from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import CreateView

from management.mixins import ManagerRequiredMixin
from management.models import Employee
from management.models.jobs import EmployeeCatalog


class AddEvaluatorView(ManagerRequiredMixin, View):

    # POST method used for giving evaluator position to employee
    def post(self, request):
        username = request.POST.get('username')
        employee = EmployeeCatalog.get_instance().get_by_username(username)
        employee.set_evaluator(True)
        return HttpResponseRedirect('/management/manageEvaluators/view/')
