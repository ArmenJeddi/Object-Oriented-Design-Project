# from django.db import models
# from django.core.exceptions import ValidationError
#
#
# class Criterion(models.Model):
#     # isQualitative = models.BooleanField()
#     name = models.CharField(max_length=50)
#
#
# class Option(models.TextField):
#     next_option = models.ForeignKey('self', default=None)
#
#
# class Range(models.Model):
#     description = models.CharField(max_length=50)
#     start = models.IntegerField()
#     end = models.IntegerField()
#     next_range = models.ForeignKey('self', default=None)
#
#
# class QualitativeCriterion(Criterion):
#     first_option = Option()
#
#     # TODO
#     def get_all_options(self):
#         pass
#
#
# class QuantitativeCriterion(Criterion):
#     first_range = Range()
#
#     # TODO
#     def get_all_range(self):
#         pass
#
#
# class QuantitativeQualitativeCriterion(QuantitativeCriterion, QualitativeCriterion):
#     pass

from django.db import models

class Option(models.Model):
    _name = models.CharField(max_length=30)
    _criterion = models.ForeignKey('EvaluationCriterion', on_delete=models.CASCADE, related_name='option_list')

class RNPMethod(models.Model):
    pass
class EvaluationCriterion(models.Model):
    _is_qualitative = models.BooleanField()
    _name = models.CharField(max_length=100)
    
