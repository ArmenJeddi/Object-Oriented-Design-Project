from django.views.generic import CreateView

from management.models import Employee
from management.mixins import ManagerRequiredMixin


class AddEmployeeView(ManagerRequiredMixin, CreateView):
    model = Employee
    template_name = 'management/addEmployee.html'
    fields = ['username', 'password', 'name', 'unit', ]
    success_url = '/management/listEmployees/'
