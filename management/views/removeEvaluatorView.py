from django.http import HttpResponseRedirect
from django.views import View

from management.mixins import ManagerRequiredMixin
from management.models.jobs import EmployeeCatalog


class RemoveEvaluatorView(ManagerRequiredMixin):

    # DELETE method used for taking back evaluator position
    def post(self, request):
        username = request.POST.get('username')
        # employee = Employee.objects.get(national_id=nid)
        employee = EmployeeCatalog.get_instance().get_by_username(username)
        employee.set_evaluator(False)
        # Evaluator.objects.get(asEmployee=employee).delete()
        return HttpResponseRedirect('/management/manageEvaluators/view/')
