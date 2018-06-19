from django.db import models
from . import Employee


class Evaluator(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='selfEvaluator')

    # TODO
    def get_evaluatee_list(self):
        # return self.evaluatee
        pass

    def add_evaluatee(self, evaluatee_NID):
        Employee.objects.get(national_id=evaluatee_NID).evaluator = self
        pass

    @classmethod
    def get_evaluator(cls, evaluator_NID):
        return cls.objects.get(employee__national_id=evaluator_NID)
