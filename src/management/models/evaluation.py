from django.db import models


class Evaluation(models.Model):
    _evaluatee = models.ForeignKey('Evaluatee', on_delete=models.CASCADE, related_name='_evaluation_list')
    _evaluation_criterion = models.ForeignKey('EvaluationCriterion', on_delete=models.CASCADE)
    _evaluator = models.ForeignKey('Evaluator', on_delete=models.CASCADE)
    _result = models.CharField(max_length=20)

    def get_result(self):
        return self._result
