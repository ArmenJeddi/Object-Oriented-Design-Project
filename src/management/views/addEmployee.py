from django.views.generic import CreateView
from ..models import Employee

class AddEmployeeView(CreateView):
    model = Employee
    template_name = 'management/addEmployee.html'
    fields = ['name', 'national_id']
    success_url = '/'