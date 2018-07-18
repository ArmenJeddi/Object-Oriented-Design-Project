from django.http import HttpResponseRedirect
from django.views import View

from auth.mixins import UserPassesTestMixin
from management.models.jobs import EmployeeCatalog
from management.status import ManagerRequired


class RemoveEvaluatorView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)



    # DELETE method used for taking back evaluator position
    def post(self, request):
        username = request.POST.get('username')
        # employee = Employee.objects.get(national_id=nid)
        employee = EmployeeCatalog.get_instance().get_by_username(username)
        employee.set_evaluator(False)
        # Evaluator.objects.get(asEmployee=employee).delete()
        return HttpResponseRedirect('/management/manageEvaluators/view/')
