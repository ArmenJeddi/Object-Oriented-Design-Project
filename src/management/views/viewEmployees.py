from django.views.generic import ListView

from management.models import Employee
from management.mixins import ManagerRequiredMixin

class EmployeeListView(ManagerRequiredMixin, ListView):

    model = Employee
    template_name = 'management/viewEmployees.html'
