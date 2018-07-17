from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template

from management.mixins import ManagerRequiredMixin
from management.models.jobs import EmployeeCatalog
from ..models import Employee


class ViewEvaluatorView(ManagerRequiredMixin, View):

    # GET method used for listing all evaluatee and evaluators
    def get(self, request):
        employee_catalog = EmployeeCatalog.get_instance()
        t = get_template('management/addEvaluator.html')
        evaluatee = employee_catalog.dump_evaluatee()
        evaluators = employee_catalog.dump_evaluator()
        print('###################', evaluatee, evaluators)
        html = t.render({'evaluatee': evaluatee, 'evaluators': evaluators}, request)
        return HttpResponse(html)
