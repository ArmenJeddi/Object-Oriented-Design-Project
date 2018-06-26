from django.db import models


class QualitativeOptions(models.Model):
    _criterion = models.ForeignKey('EvaluationCriterion', on_delete=models.CASCADE, related_name='qualitative_list')
    _name = models.CharField(max_length=20)


class QuantitativeOption(models.Model):
    _criterion = models.ForeignKey('EvaluationCriterion', on_delete=models.CASCADE, related_name='quantitative_list')
    _name = models.CharField(max_length=20)
    _beginning = models.IntegerField()
    _end = models.IntegerField()


# TODO
class RNPMethod(models.Model):
    pass


class EvaluationCriterion(models.Model):
    _is_qualitative = models.BooleanField()
    _is_quantitative = models.BooleanField()
    _name = models.CharField(max_length=100)
