from django.db import models

from auth.models import User
from management.models import Evaluatee


class Employee(User):
    # asEvaluator = models.OneToOneField('Evaluator', on_delete=models.SET_NULL, null=True)
    # asEvaluatee = models.OneToOneField('Evaluatee', on_delete=models.SET_NULL, null=True)
    _unit = models.CharField(max_length=20, null=True)

    # user_ptr = models.OneToOneField('User', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        as_evaluatee = Evaluatee.objects.create(_asEmployee=self)
        as_evaluatee.save()

    def get_unit(self):
        return self._unit

    def get_as_evaluatee(self):
        return self._asEvaluatee

    @classmethod
    def dump_evaluator_employee(cls):
        data = []
        for evaluator in cls.objects.filter(_asEvaluator__isnull=False):
            name = evaluator.get_name()
            nid = evaluator.get_id()
            data.append({'name': name, 'username': nid})
        return data

    @classmethod
    def dump_evaluatee_employee(cls):
        data = []
        for evaluatee in cls.objects.filter(_asEvaluatee__isnull=False):
            name = evaluatee.get_name()
            nid = evaluatee.get_id()
            data.append({'name': name, 'username': nid})
        return data

    @classmethod
    def get_by_username(cls, username):
        return cls.objects.get(_username=username)

    @classmethod
    def create(cls, username, password, name, unit):
        e = Employee(_username=username, _password=password, _name=name, _unit=unit)
        e.save()

    @classmethod
    def dump_all(cls):
        data = []
        for employee in cls.objects.all():
            name = employee.get_name()
            username = employee.get_id()
            data.append({'name': name, 'username': username})
        return data

    @classmethod
    def remove_by_username(cls, nid):
        cls.objects.get(_username=nid).delete()

