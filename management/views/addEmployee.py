from django.views.generic import CreateView

from management.models import Employee
from management.mixins import ManagerRequiredMixin


class AddEmployeeView(ManagerRequiredMixin, CreateView):
    model = Employee
    template_name = 'management/addEmployee.html'
    fields = ['_username', '_password', '_name', '_unit', ]
    success_url = '/management/listEmployees/'
