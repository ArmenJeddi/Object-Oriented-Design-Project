from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from auth.mixins import UserPassesTestMixin
from management.models.jobs import EmployeeCatalog
from management.status import ManagerRequired


class ViewEvaluationView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)

    def get(self, request):
        t = get_template('management/viewEvaluation.html')
        evaluatees = EmployeeCatalog.get_instance().dump_evaluatee()
        html = t.render({'evaluatees': evaluatees}, request)
        return HttpResponse(html)
