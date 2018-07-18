import json

from django.http import HttpResponseRedirect
from django.views import View

from management.mixins import ManagerRequiredMixin
from management.models.assignment import AssignmentCatalog


class RemoveAssignmentView(ManagerRequiredMixin):

    def post(self, request):
        json_data = json.loads(request.body)
        evaluatee_username = json_data['evaluatee_username']
        evaluator_username = json_data['evaluator_username']
        AssignmentCatalog.get_instance().remove_assignment(evaluatee_username, evaluator_username)
        return HttpResponseRedirect('/management/assignEvaluatorToEmployee/')
