from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template
from django.views import View
from django.views.generic import CreateView

from management.mixins import ManagerRequiredMixin
from management.models import EvaluationCriterion
from management.models.criterion import QuantitativeOption, QualitativeOptions, CriterionCatalog
import json


class RemoveCriterionView(ManagerRequiredMixin, View):
    def get(self, request, criterion_name):
        CriterionCatalog.get_instance().delete_if_exists(criterion_name)
        return redirect('/management/viewCriterion/')
