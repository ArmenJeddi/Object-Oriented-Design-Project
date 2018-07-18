import json

from django.http import HttpResponseRedirect
from django.views import View

from auth.mixins import UserPassesTestMixin
from auth.models import UserCatalog
from management.models.jobs import Employee
from management.status import ManagerRequired


class EmployeeDeleteView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)

    # DELETE method used for taking back evaluator position
    def post(self, request):
        nid = json.loads(request.body)['username']
        # employee = Employee.objects.get(national_id=nid)
        user = UserCatalog.get_instance().get_by_username(nid)
        if user.get_job().get_title() == Employee.get_title():
            UserCatalog.get_instance().delete_by_username(nid)
        # Evaluator.objects.get(asEmployee=employee).delete()
        return HttpResponseRedirect('/')
