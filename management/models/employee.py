from django.db import models
from auth.models import User


class Employee(User):
    _unit = models.CharField(max_length=20, null=True)
    _is_evaluator = models.BooleanField(default=False, null=False)

    def get_unit(self):
        return self._unit

    def set_as_evaluator(self):
        self._is_evaluator = True
        self.save()

    def set_as_evaluatee(self):
        self._is_evaluator = False
        self.save()

    @classmethod
    def dump_evaluator(cls):
        data = []
        for evaluator in cls.objects.filter(_is_evaluator=True):
            name = evaluator.get_name()
            nid = evaluator.get_id()
            data.append({'name': name, 'username': nid})
        return data

    @classmethod
    def dump_evaluatee(cls):
        data = []
        for evaluatee in cls.objects.filter(_is_evaluator=False):
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

    @classmethod
    def set_as_evaluator(cls, username):
        employee = cls.objects.get(_username=username)
        employee.set_as_evaluator()

    @classmethod
    def _set_as_evaluatee(cls, username):
        employee = cls.objects.get(_username=username)
        employee.set_as_evaluatee()
