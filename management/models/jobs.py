from django.db import models
from auth.models import Job, JobCatalog
from management.models.assignment import AssignmentCatalog
from rnp.decorators import singleton


@singleton
class ManagerCatalog(JobCatalog):

    def create(self, user):
        manager = Manager(_user=user)
        manager.full_clean()
        manager.save(force_insert=True)
        user.set_job(manager)
        return manager


class Manager(Job):
    _TITLE = 'Manager'

    objects = ManagerCatalog.get_instance()


Job.set_job_catalog(Manager.get_title(), ManagerCatalog.get_instance())


@singleton
class EmployeeCatalog(JobCatalog):

    def create(self, user, unit, is_evaluator=False):
        employee = Employee(_unit=unit, _user=user, _is_evaluator=is_evaluator)
        employee.full_clean()
        employee.save(force_insert=True)
        user.set_job(employee)
        return employee

    def dump_evaluatee(self):
        data = []
        for job in self.filter(_is_evaluator=False):
            evaluatee = job.get_user()
            data.append({
                'username': evaluatee.get_username(),
                'name': evaluatee.get_name()
            })
        return data

    def dump_evaluator(self):
        data = []
        for job in self.filter(_is_evaluator=True):
            evaluator = job.get_user()
            data.append({
                'username': evaluator.get_username(),
                'name': evaluator.get_name()
            })
        return data

    def dump_all(self):
        data = []
        for job in self.all():
            employee = job.get_user()
            data.append({
                'username': employee.get_username(),
                'name': employee.get_name()
            })
        return data


class Employee(Job):
    _TITLE = 'Employee'

    _unit = models.CharField(max_length=20)
    _is_evaluator = models.BooleanField(default=False)

    objects = EmployeeCatalog.get_instance()

    def get_unit(self):
        return self._unit

    def is_evaluator(self):
        return self._is_evaluator

    def set_evaluator(self, value):
        self._is_evaluator = value
        if not value:
            AssignmentCatalog.get_instance().remove_by_evaluator(self.get_user())
        self.full_clean()
        self.save()


Job.set_job_catalog(Employee.get_title(), EmployeeCatalog.get_instance())
