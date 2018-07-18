from django.http import HttpResponseRedirect
from django.views import View

from auth.mixins import UserPassesTestMixin
from management.models.jobs import EmployeeCatalog
from management.status import ManagerRequired


class AddEvaluatorView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)

    # POST method used for giving evaluator position to employee
    def post(self, request):
        username = request.POST.get('username')
        employee = EmployeeCatalog.get_instance().get_by_username(username)
        employee.set_evaluator(True)
        return HttpResponseRedirect('/management/manageEvaluators/view/')
