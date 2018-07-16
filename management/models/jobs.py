from django.db import models
from auth.models import User, Job, JobCatalog
from rnp.decorators import singleton

@singleton
class ManagerCatalog(JobCatalog):

    def get_by_username(self, username):
        return self.get(_user=username)

    def create(self, user):
        manager = Manager(_user=user)
        manager.save()
        return manager

    def delete_by_username(self, username):
        self.get(_user=username).delete()
    
class Manager(Job):

    TITLE = 'Manager'

    objects = ManagerCatalog.get_instance()

Job.set_job_catalog(Manager.TITLE, ManagerCatalog.get_instance())

@singleton
class EmployeeCatalog(JobCatalog):

    def get_by_username(self, username):
        return self.get(_user=username)

    def create(self, user, unit, is_evaluator=False):
        employee = Employee(_unit=unit, _user=user, _is_evaluator=is_evaluator)
        employee.save()
        return employee

    def delete_by_username(self, username):
        self.get(_user=username).delete()

class Employee(Job):

    TITLE = 'Employee'
    
    _unit = models.CharField(max_length=20, null=True)
    _is_evaluator = models.BooleanField(default=False, null=False)

    objects = EmployeeCatalog.get_instance()

    def get_unit(self):
        return self._unit

    def is_evaluator(self):
        return self._is_evaluator

    def set_evaluator(self, value):
        self._is_evaluator = value
        self.save()

Job.set_job_catalog(Employee.TITLE, EmployeeCatalog.get_instance())
