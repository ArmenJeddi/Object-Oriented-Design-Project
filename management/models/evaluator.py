from django.db import models

from management.models.evaluation import Evaluation


class Evaluator(models.Model):

    def evaluate_employee(self, evaluatee, evaluation_criterion, result):
        return Evaluation(evaluation_criterion=evaluation_criterion, result=result, evaluator=self, evaluatee=evaluatee)

    def add_evaluatee(self, evaluatee):
        evaluatee.evaluator = self

    def get_evaluatee_list(self):
        return self._evaluatee_list
