from django.db import models
from auth.models import User, Job

class Manager(Job):

    TITLE = 'Manager'

    def __init__(self, user):
        super().__init__(user)

Job.set_job_factory(Manager, Manager)

class Employee(Job):

    TITLE = 'Employee'

    class EmployeeModel(models.Model):
        _unit = models.CharField(max_length=20, null=True)
        _is_evaluator = models.BooleanField(default=False, null=False)
        _user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')

        def get_unit(self):
            return self._unit

        def is_evaluator(self):
            return self._is_evaluator

        def set_evaluator(self, value):
            self._is_evaluator = value
            self.save()

        def get_user(self):
            return self.user

    def __init__(self, user, unit=None, is_evaluator=False):
        super().__init__(user)
        try:
            self._model = self.EmployeeModel.objects.get(_user=user)
        except self.EmployeeModel.DoesNotExist:
            self._model = self.EmployeeModel(_unit=unit, _is_evaluator=is_evaluator)

    def save(self):
        super().save()
        self._model.save()

    def delete(self):
        super().delete()
        self._model.delete()

    def get_unit(self):
        return self._model.get_unit()

    def is_evaluator(self):
        return self._model.is_evaluator()
    
    def set_evaluator(self, value):
        self._model.set_evaluator(value)

    @classmethod
    def dump_evaluator(cls):
        data = []
        for evaluator in cls.EmployeeModel.objects.filter(_is_evaluator=True):
            name = evaluator.get_user().get_name()
            nid = evaluator.get_user().get_username()
            data.append({'name': name, 'username': nid})
        return data

    @classmethod
    def dump_evaluatee(cls):
        data = []
        for evaluatee in cls.EmployeeModel.objects.filter(_is_evaluator=False):
            name = evaluatee.get_user().get_name()
            nid = evaluatee.get_user().get_username()
            data.append({'name': name, 'username': nid})
        return data

    @classmethod
    def dump_all(cls):
        data = []
        for employee in cls.EmployeeModel.objects.all():
            name = employee.get_user().get_name()
            username = employee.get_user().get_username()
            data.append({'name': name, 'username': username})
        return data

    

Job.set_job_factory(Employee, Employee)
