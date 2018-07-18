import json

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.views import View

from auth.models import UserCatalog, User
from management.mixins import ManagerRequiredMixin
from management.models.jobs import Employee


class EmployeeDeleteView(ManagerRequiredMixin, View):

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
