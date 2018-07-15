from django.db import models

from management.models import Employee


class Assignment(models.Model):
    _evaluator = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, related_name='_evaluator_assignment')
    _evaluatee = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, related_name='_evaluatee_assignment')

    class Meta:
        unique_together = ('_evaluator', '_evaluatee')

    @classmethod
    def get_evaluatee_list(cls, evaluator):
        data = []
        for evaluatee in cls.objects.filter(_evaluator=evaluator):
            data.append({
                'name': evaluatee.get_name(),
                'username': evaluatee.get_username,
            })
        return data

    @classmethod
    def add_assignment(cls, evaluator_username, evaluatee_username):
        evaluator = Employee.get_by_username(evaluator_username)
        evaluatee = Employee.get_by_username(evaluatee_username)
        assignment = Assignment(_evaluator=evaluator, _evaluatee=evaluatee)
        assignment.save()
