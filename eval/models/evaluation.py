from django.db import models
from auth.models import User

class EvaluationCatalog(models.Manager):

    def evaluate_employee(self, evaluatee, evaluation_criterion, evaluator, qualitative_result, quantitative_result):
        evaluation = Evaluation(_evaluatee=evaluatee,
                                _evaluation_criterion=evaluation_criterion,
                                _evaluator=evaluator,
                                _qualitative_result=qualitative_result,
                                _quantitative_result=quantitative_result)
        evaluation.save()

        
class Evaluation(models.Model):
    _evaluatee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    _evaluation_criterion = models.ForeignKey('management.EvaluationCriterion', on_delete=models.CASCADE)
    _evaluator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    _qualitative_result = models.CharField(max_length=20)
    _quantitative_result = models.CharField(max_length=20)

    objects = EvaluationCatalog()
    
    def get_qualitative_result(self):
        return self._qualitative_result

    def get_quantitative_result(self):
        return self._quantitative_result

    def get_criterion_name(self):
        return self._evaluation_criterion.get_name()
