from django.db import models

from eval.models.evaluation import Evaluation
from management.models import Employee
from management.models.evaluatee import Evaluatee


class Evaluator(models.Model):
    _asEmployee = models.OneToOneField('Employee', on_delete=models.CASCADE, related_name='_asEvaluator')

    def evaluate_employee(self, evaluatee, evaluation_criterion, quantitative_result, qualitative_result):
        return Evaluation(
            evaluation_criterion=evaluation_criterion,
            quantitative_result=quantitative_result,
            qualitative_result=qualitative_result,
            evaluator=self,
            evaluatee=evaluatee)

    def add_evaluatee(self, evaluatee):
        evaluatee._evaluator = self

    def dump_evaluatee_list(self):
        dump_data = []
        for evaluatee in self._evaluatee_list:
            dump_data.append({
                'id': evaluatee.asEmployee_id,
                'name': evaluatee.asEmployee_name,
            })
        return dump_data

    @classmethod
    def get_by_username(cls, username):
        return cls.objects.get(_asEmployee___username=username)

    @classmethod
    def is_evaluator(cls, user):
        return cls.objects.filter(_asEmployee___username=user.get_id()).count() == 1

    @classmethod
    def delete_by_username(cls, username):
        cls.objects.get(_asEmployee___username=username).delete()

    @classmethod
    def create_by_username(cls, username):
        employee = Employee.get_by_username(username)
        Evaluatee.remove_by_username(username)
        # employee.set_as_evaluator()
        cls.objects.create(_asEmployee=employee).save()
