from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from django.views.generic import CreateView

from auth.mixins import LoginRequiredMixin
from management.mixins import ManagerRequiredMixin
from management.models import EvaluationCriterion
from management.models.criterion import QuantitativeOption, QualitativeOptions
import json


class ViewEvaluationView(ManagerRequiredMixin, View):
    def get(self, request):
        evaluatee = self.get_employee().get_as_evaluatee()
        evaluation_list = evaluatee.dump_evaluation_list()
        t = get_template('management/viewEvaluation.html')
        html = t.render(evaluation_list, request)
        return HttpResponse(html)

#   [
#   {}
#   ]