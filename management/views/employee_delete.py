import json

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.views import View

from auth.models import UserCatalog, User
from auth.mixins import UserPassesTestMixin
from management.models.jobs import Employee
from management.status import ManagerRequired


class EmployeeDeleteView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)

    def post(self, request):
        nid = json.loads(request.body)['username']
        try:
            user = UserCatalog.get_instance().get_by_username(nid)
        except User.DoesNotExist:
            return HttpResponseBadRequest()
        if user.get_job_title() == Employee.get_title():
            UserCatalog.get_instance().delete_by_username(nid)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseBadRequest()
