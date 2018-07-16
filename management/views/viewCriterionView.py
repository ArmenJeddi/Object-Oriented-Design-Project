from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from django.views.generic import CreateView

from auth.mixins import LoginRequiredMixin
from management.mixins import ManagerRequiredMixin
from management.models import EvaluationCriterion
from management.models.criterion import QuantitativeOption, QualitativeOptions, CriterionCatalog
import json


class ViewCriterionView(LoginRequiredMixin, View):
    def get(self, request):
        criterion_names = CriterionCatalog.get_instance().get_names()
        t = get_template('management/viewCriterion.html')
        html = t.render({'criterion_names':criterion_names}, request)
        return HttpResponse(html)
