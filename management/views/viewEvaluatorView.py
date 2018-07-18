from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from auth.mixins import UserPassesTestMixin
from management.models.jobs import EmployeeCatalog
from management.status import ManagerRequired


class ViewEvaluatorView(UserPassesTestMixin):

    def __init__(self, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, **kwargs)

    def get(self, request):
        employee_catalog = EmployeeCatalog.get_instance()
        t = get_template('management/addEvaluator.html')
        evaluatee = employee_catalog.dump_evaluatee()
        evaluators = employee_catalog.dump_evaluator()
        print('###################', evaluatee, evaluators)
        html = t.render({'evaluatee': evaluatee, 'evaluators': evaluators}, request)
        return HttpResponse(html)
