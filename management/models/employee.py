from django.db import models

from auth.models import User


class Employee(User):
    asEvaluator = models.OneToOneField('Evaluator', on_delete=models.SET_NULL, null=True)
    asEvaluatee = models.OneToOneField('Evaluatee', on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=20)

    def get_unit(self):
        return self.unit
