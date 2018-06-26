from django.db import models

from management.models.evaluation import Evaluation


class Evaluator(models.Model):
    asEmployee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='asEvaluator')
    def evaluate_employee(self, evaluatee, evaluation_criterion, result):
        return Evaluation(evaluation_criterion=evaluation_criterion, result=result, evaluator=self, evaluatee=evaluatee)

    def add_evaluatee(self, evaluatee):
        evaluatee.evaluator = self

    # TODO
    def get_evaluatee_list(self):
        return self._evaluatee_list
