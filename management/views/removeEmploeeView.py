import json

from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import DeleteView

from management.mixins import ManagerRequiredMixin
from ..models import Employee, Evaluator


class RemoveEmployeeView(ManagerRequiredMixin, View):

    # DELETE method used for taking back evaluator position
    def post(self, request):
        nid = json.loads(request.body)['username']
        # employee = Employee.objects.get(national_id=nid)
        Employee.delete_by_nid(nid)
        # Evaluator.objects.get(asEmployee=employee).delete()
        return HttpResponseRedirect('/')