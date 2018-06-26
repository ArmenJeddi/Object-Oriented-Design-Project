from django.db import models

from auth.models import User
from management.models import Evaluatee


class Employee(User):
    # asEvaluator = models.OneToOneField('Evaluator', on_delete=models.SET_NULL, null=True)
    # asEvaluatee = models.OneToOneField('Evaluatee', on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=20, null=True)

    # user_ptr = models.OneToOneField('User', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        as_evaluatee = Evaluatee.objects.create(asEmployee=self)
        as_evaluatee.save()

    def get_unit(self):
        return self.unit

    @classmethod
    def get_all_evaluator_employee(cls):
        return cls.objects.filter(asEvaluator__isnull=False)

    @classmethod
    def get_all_evaluatee_employee(cls):
        return cls.objects.filter(asEvaluatee__isnull=False)
