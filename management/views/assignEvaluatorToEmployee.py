import json

from django.views import View
from django.http import HttpResponse
from django.template.loader import get_template

from management.mixins import ManagerRequiredMixin
from management.models.assignment import Assignment, AssignmentCatalog
from management.models.jobs import EmployeeCatalog
from ..models import Employee


class AssignEvaluatorToEmployee(ManagerRequiredMixin, View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = get_template('management/assignEvaluatorToEmployee.html')

    def get(self, request):
        employee_catalog = EmployeeCatalog.get_instance()
        evaluatees = employee_catalog.dump_evaluatee()
        evaluators = employee_catalog.dump_evaluator()
        html = self.template.render({
            'evaluatees': evaluatees,
            'evaluators': evaluators,
        }, request)
        return HttpResponse(html)

    def post(self, request):
        json_data = json.loads(request.body)
        evaluator_username = json_data['evaluator_username']
        evaluatee_username = json_data['evaluatee_username']
        AssignmentCatalog.add_assignment(evaluatee_username=evaluatee_username, evaluator_username=evaluator_username)
