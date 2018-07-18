from django.db import models

from auth.models import UserCatalog, User
from management.models import Employee
from management.models.jobs import EmployeeCatalog
from rnp.decorators import singleton


@singleton
class AssignmentCatalog(models.Manager):

    def get_evaluatee_list(self, evaluator):
        data = []
        for assignment in self.filter(_evaluator=evaluator):
            data.append({
                'name': assignment.get_evaluatee_name(),
                'username': assignment.get_evaluatee_username(),
            })
        return data

    def add_assignment(self, evaluator_username, evaluatee_username):
        evaluator = UserCatalog.get_instance().get_by_username(evaluator_username)
        evaluatee = UserCatalog.get_instance().get_by_username(evaluatee_username)
        assignment = Assignment(_evaluator=evaluator, _evaluatee=evaluatee)
        assignment.save()

    def remove_assignment(self, evaluatee_username, evaluator_username):
        evaluator = UserCatalog.get_instance().get_by_username(evaluator_username)
        evaluatee = UserCatalog.get_instance().get_by_username(evaluatee_username)
        self.get(_evaluator=evaluator, _evaluatee=evaluatee).delete()

    def dump_all(self):
        data = []
        for assignment in self.all():
            data.append({
                'evaluatee_name': assignment.get_evaluatee_name(),
                'evaluatee_username': assignment.get_evaluatee_username(),
                'evaluator_name': assignment.get_evaluator_name(),
                'evaluator_username': assignment.get_evaluator_username(),
            })
        return data


class Assignment(models.Model):
    objects = AssignmentCatalog.get_instance()
    _evaluator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_evaluator_assignment')
    _evaluatee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_evaluatee_assignment')

    class Meta:
        unique_together = ('_evaluator', '_evaluatee')

    def get_evaluatee_name(self):
        return self._evaluatee.get_name()

    def get_evaluatee_username(self):
        return self._evaluatee.get_username()

    def get_evaluator_name(self):
        return self._evaluator.get_name()

    def get_evaluator_username(self):
        return self._evaluator.get_username()
