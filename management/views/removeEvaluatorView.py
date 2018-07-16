from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import DeleteView

from management.mixins import ManagerRequiredMixin
from ..models import Employee
from management.models.evaluator import Evaluator


class RemoveEvaluatorView(ManagerRequiredMixin, View):

    # DELETE method used for taking back evaluator position
    def post(self, request):
        nid = request.POST.get('username')
        # employee = Employee.objects.get(national_id=nid)
        Evaluator.delete_by_username(nid)
        # Evaluator.objects.get(asEmployee=employee).delete()
        return HttpResponseRedirect('/management/manageEvaluators/view/')
