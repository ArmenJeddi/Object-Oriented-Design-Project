import json

from django.views import View
from django.http import HttpResponseRedirect

from management.mixins import ManagerRequiredMixin
from management.models.jobs import Employee
from auth.models import UserCatalog


class EmployeeDeleteView(ManagerRequiredMixin, View):

    # DELETE method used for taking back evaluator position
    def post(self, request):
        nid = json.loads(request.body)['username']
        # employee = Employee.objects.get(national_id=nid)
        user = UserCatalog.get_instance().get_by_username(nid)
        if user.get_job().TITLE == Employee.TITLE:
            UserCatalog.get_instance().delete_by_username(nid)
        # Evaluator.objects.get(asEmployee=employee).delete()
        return HttpResponseRedirect('/')
