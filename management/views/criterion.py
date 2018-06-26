from django.views.generic import CreateView
from ..models import Criterion


class Criterion(CreateView):
    model = Criterion
    template_name = 'management/addEmployee.html'
    fields = ['name', 'national_id']
    success_url = '/'
