from django.db import models
from . import Employee, Evaluation

class Evaluator(models.Model):
    
    def evaluate_employee(self, evaluatee, evaluation_criterion, result):
        return Evaulation(evaluation_criterion=evaluation_criterion, result=result, evaluator=self, evaluatee=evaluatee)

    def add_evaluatee(self, evaluatee):
        evaluatee.evaluator = self

    def get_evaluatee_list(self):
        return self._evaluatee_list
