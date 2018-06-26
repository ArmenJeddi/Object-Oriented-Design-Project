from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from django.views.generic import CreateView

from management.mixins import ManagerRequiredMixin
from management.models import EvaluationCriterion
from management.models.criterion import QuantitativeOption, QualitativeOptions
import json


class ViewCriterionView(ManagerRequiredMixin, View):
    def get(self, request):
        criterion_names = EvaluationCriterion.get_names()
        t = get_template('management/viewCriterion.html')
        html = t.render(criterion_names, request)
        return HttpResponse(html)
