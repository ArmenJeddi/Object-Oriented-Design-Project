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
    _name = models.CharField(max_length=100)
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

    def set_reward_method(self, reward_method):
        self._reward = reward_method
        self.save()

    def set_punishment_method(self, punishment_method):
        self._punishment = punishment_method
        self.save()

    @classmethod
    def get_names(cls):
        return list(cls.objects.all().values_list('_name', flat=True))

    @classmethod
    def get_by_name(cls, criterion_name: object):
        return cls.objects.get(_name=criterion_name)

    @classmethod
    def dump_all(cls):
        criterion_array = []
        for criterion in cls.objects.all():
            criterion_array.append(criterion.dump())
        return criterion_array

    def get_name(self):
        return self._name

