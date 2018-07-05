from django.db import models


class QualitativeOptions(models.Model):
    _criterion = models.ForeignKey('EvaluationCriterion', on_delete=models.CASCADE, related_name='qualitative_list')
    _name = models.CharField(max_length=20)

    def get_name(self):
        return self._name


class QuantitativeOption(models.Model):
    _criterion = models.ForeignKey('EvaluationCriterion', on_delete=models.CASCADE, related_name='quantitative_list')
    _name = models.CharField(max_length=20)
    _beginning = models.IntegerField()
    _end = models.IntegerField()

    def get_name(self):
        return self._name

    def get_beginning(self):
        return self._beginning

    def get_end(self):
        return self._end


# # TODO
# class RNPMethod(models.Model):
#     pass


class EvaluationCriterion(models.Model):
    _is_qualitative = models.BooleanField(default=False)
    _is_quantitative = models.BooleanField(default=True)
    _name = models.CharField(max_length=100, unique=True)
    _reward = models.CharField(max_length=100, null=True)
    _punishment = models.CharField(max_length=100, null=True)

    def dump(self):
        qualitative_values = []
        quantitative_values = []
        for val in self.qualitative_list:
            qualitative_values.append(val.get_name())
        for val in self.quantitative_list:
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

    def get_reward(self):
        return self._reward

    def get_punishment(self):
        return self._punishment

    @classmethod
    def set_reward_method(cls, criterion_name, reward_method):
        criterion = cls.objects.get(_name=criterion_name)
        criterion._reward = reward_method
        criterion.save()

    @classmethod
    def set_punishment_method(cls, criterion_name, punishment_method):
        criterion = cls.objects.get(_name=criterion_name)
        criterion._punishment = punishment_method
        criterion.save()

    @classmethod
    def get_names(cls):
        return list(cls.objects.all().values_list('_name', flat=True))

    # @classmethod
    # def get_by_name(cls, criterion_name: object):
    #     return cls.objects.get(_name=criterion_name)

    @classmethod
    def dump_all(cls):
        criterion_array = []
        for criterion in cls.objects.all():
            criterion_array.append(criterion.dump())
        return criterion_array

    @classmethod
    def dump_by_name(cls, name):
        return cls.objects.get(_name=name).dump()

    def get_name(self):
        return self._name

    def get_is_qualitative(self):
        return self._is_qualitative

    def get_is_quantitative(self):
        return self._is_quantitative

    @classmethod
    def delete_if_exists(cls, criterion_name):
        if cls.objects.filter(_name=criterion_name).count() != 0:
            cls.objects.get(_name=criterion_name).delete()

    @classmethod
    def get_names_and_rnp(cls):
        criteria = []
        for criterion in cls.objects.all():
            criteria.append({
                'name': criterion.get_name(),
                'reward': criterion.get_reward(),
                'punishment': criterion.get_punishment()
            })
