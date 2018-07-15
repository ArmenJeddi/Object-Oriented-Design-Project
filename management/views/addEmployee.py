import json

from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.views import View
from django.views.generic import CreateView

from management.models import Employee
from management.mixins import ManagerRequiredMixin


class AddEmployeeView(ManagerRequiredMixin, View):

    def get(self, request):
        t = get_template('management/addEmployee.html')
        html = t.render({}, request)
        return HttpResponse(html)

    def post(self, request):
        json_data = json.loads(request.body)
        username = json_data['username']
        password = json_data['password']
        name = json_data['name']
        unit = json_data['unit']
        Employee.create(username, password, name, unit)
        return HttpResponseRedirect('/')
