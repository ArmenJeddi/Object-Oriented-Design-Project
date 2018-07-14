from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView

from management.models import Employee
from management.mixins import ManagerRequiredMixin


class AddEmployeeView(ManagerRequiredMixin, View):
    model = Employee

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        unit = request.POST.get('unit')
        Employee.create(username, password, name, unit)
        return HttpResponseRedirect('/')
    # template_name = 'management/addEmployee.html'
    # fields = ['username', 'password', 'name', 'unit', ]
    # success_url = '/management/listEmployees/'
