from django.shortcuts import render
from django.views.generic.base import View

from auth.mixins import UserPassesTestMixin
from management.models.jobs import EmployeeCatalog
from management.status import ManagerRequired


class EmployeeListView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)

    http_method_names = ('get',)
    
    def get(self, request):
        context = {
            'employees': EmployeeCatalog.get_instance().dump_all()
        }
        return render(request, 'management/viewEmployees.html', context)
