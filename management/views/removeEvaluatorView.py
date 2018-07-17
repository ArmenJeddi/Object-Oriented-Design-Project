from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import DeleteView

from management.mixins import ManagerRequiredMixin
from management.models.jobs import EmployeeCatalog
from ..models import Employee


class RemoveEvaluatorView(ManagerRequiredMixin, View):

    # DELETE method used for taking back evaluator position
    def post(self, request):
        username = request.POST.get('username')
        # employee = Employee.objects.get(national_id=nid)
        employee = EmployeeCatalog.get_by_username(username)
        employee.set_evaluator(False)
        # Evaluator.objects.get(asEmployee=employee).delete()
        return HttpResponseRedirect('/management/manageEvaluators/view/')
