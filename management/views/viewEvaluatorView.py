from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template

from management.mixins import ManagerRequiredMixin
from ..models import Employee, Evaluator


class ViewEvaluatorView(ManagerRequiredMixin, View):

    # GET method used for listing all evaluatee and evaluators
    def get(self, request):
        t = get_template('management/addEvaluator.html')
        evaluatee = Employee.get_all_evaluatee_employee()
        evaluators = Employee.get_all_evaluator_employee()
        html = t.render({'evaluatee': evaluatee, 'evaluators': evaluators}, request)
        return HttpResponse(html)
