from django.db import models

from management.models import Employee
from rnp.decorators import singleton


@singleton
class AssignmentCatalog(models.Manager):

    def get_evaluatee_list(self, evaluator):
        data = []
        for evaluatee in self.filter(_evaluator=evaluator):
            data.append({
                'name': evaluatee.get_name(),
                'username': evaluatee.get_username,
            })
        return data

    @staticmethod
    def add_assignment(evaluator_username, evaluatee_username):
        evaluator = UserCatalog.get_instance().get_by_username(evaluator_username)
        evaluatee = UserCatalog.get_instance().get_by_username(evaluatee_username)
        assignment = Assignment(_evaluator=evaluator, _evaluatee=evaluatee)
        assignment.save()


class Assignment(models.Model):
    objects = AssignmentCatalog.get_instance()
    _evaluator = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, related_name='_evaluator_assignment')
    _evaluatee = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, related_name='_evaluatee_assignment')

    class Meta:
        unique_together = ('_evaluator', '_evaluatee')
