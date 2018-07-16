import json

from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

from management.mixins import ManagerRequiredMixin


class RemoveEmployeeView(ManagerRequiredMixin, View):

    # DELETE method used for taking back evaluator position
    def post(self, request):
        nid = json.loads(request.body)['username']
        # employee = Employee.objects.get(national_id=nid)
        Employee.remove_by_username(nid)
        # Evaluator.objects.get(asEmployee=employee).delete()
        return HttpResponseRedirect('/')
