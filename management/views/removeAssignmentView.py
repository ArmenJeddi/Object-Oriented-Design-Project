import json

from django.http import HttpResponseRedirect
from django.views import View

from auth.mixins import UserPassesTestMixin
from management.models.assignment import AssignmentCatalog
from management.status import ManagerRequired


class RemoveAssignmentView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)

    def post(self, request):
        json_data = json.loads(request.body)
        evaluatee_username = json_data['evaluatee_username']
        evaluator_username = json_data['evaluator_username']
        print(evaluatee_username, evaluator_username)
        AssignmentCatalog.get_instance().remove_assignment(evaluatee_username, evaluator_username)
        return HttpResponseRedirect('/management/assignEvaluatorToEmployee/')
