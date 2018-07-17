from django.db import models

from rnp.decorators import singleton


class QualitativeOptions(models.Model):
    _criterion = models.ForeignKey('EvaluationCriterion', on_delete=models.CASCADE, related_name='_qualitative_list')
    _name = models.CharField(max_length=20)

    def get_name(self):
        return self._name


class QuantitativeOption(models.Model):
    _criterion = models.ForeignKey('EvaluationCriterion', on_delete=models.CASCADE, related_name='_quantitative_list')
    _name = models.CharField(max_length=20)
    _beginning = models.IntegerField()
    _end = models.IntegerField()

    def get_name(self):
        return self._name

    def get_beginning(self):
        return self._beginning

    def get_end(self):
        return self._end


@singleton
class CriterionCatalog(models.Manager):

    def get_names(self):
        names = []
        for criterion in self.all():
            names.append(criterion.get_name())
        return names

    def dump_all(self):
        criterion_array = []
        for criterion in self.all():
            criterion_array.append(criterion.dump())
        return criterion_array

    def dump_by_name(self, name):
        return self.get(_name=name).dump()

    def get_by_name(self, name):
        return self.get(_name=name)

    def delete_if_exists(self, criterion_name):
        if self.filter(_name=criterion_name).count() != 0:
            self.get(_name=criterion_name).delete()

    def get_names_and_rnp(self):
        criteria = []
        for criterion in self.all():
            criteria.append({
                'name': criterion.get_name(),
                'reward': criterion.get_reward(),
                'punishment': criterion.get_punishment()
            })

        return criteria


class EvaluationCriterion(models.Model):
    objects = CriterionCatalog.get_instance()
    _is_qualitative = models.BooleanField(default=False)
    _is_quantitative = models.BooleanField(default=True)
    _name = models.CharField(max_length=100, unique=True)
    _reward = models.CharField(max_length=100, null=True)
    _punishment = models.CharField(max_length=100, null=True)

    def dump(self):
        qualitative_values = []
        quantitative_values = []
        for val in self._qualitative_list.all():
            qualitative_values.append(val.get_name())
        for val in self._quantitative_list.all():
            quantitative_values.append({
                'name': val.get_name(),
                'beginning': val.get_beginning(),
                'end': val.get_end()
            })
        data = {
            'name': self._name,
            'qualitative': qualitative_values,
            'quantitative': quantitative_values
        }
        return data

    def set_reward(self, reward):
        self._reward = reward

    def get_reward(self):
        return self._reward

    def set_punishment(self, punishment):
        self._punishment = punishment

    def get_punishment(self):
        return self._punishment

    def get_name(self):
        return self._name

    def get_is_qualitative(self):
        return self._is_qualitative

    def get_is_quantitative(self):
        return self._is_quantitative

