from django.views.generic import UpdateView
from ..models import Employee

class EmployeeEditView(UpdateView):
    model = Employee
    template_name = 'management/editEmployee.html'
    fields = ['name']
    success_url = '/'