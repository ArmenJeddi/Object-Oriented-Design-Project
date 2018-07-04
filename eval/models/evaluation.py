from django.db import models


class Evaluation(models.Model):
    _evaluatee = models.ForeignKey('management.Evaluatee', on_delete=models.CASCADE, related_name='_evaluation_list')
    _evaluation_criterion = models.ForeignKey('management.EvaluationCriterion', on_delete=models.CASCADE)
    _evaluator = models.ForeignKey('management.Evaluator', on_delete=models.CASCADE)
    _qualitative_result = models.CharField(max_length=20)
    _quantitative_result = models.CharField(max_length=20)

    def get_qualitative_result(self):
        return self._qualitative_result

    def get_quantitative_result(self):
        return self._quantitative_result

    def get_criterion_name(self):
        return self._evaluation_criterion.get_name()
