from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from eval.mixins import EvaluatorRequiredMixin, EvaluateeRequiredMixin
from eval.models.evaluation import EvaluationCatalog
from management.mixins import ManagerRequiredMixin
from management.models import EvaluationCriterion
import json


class AllEvaluationResultView(ManagerRequiredMixin, View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = get_template('management/allEvaluationResult.html')

    def get(self, request):
        data = EvaluationCatalog.get_instance().dump_all()
        html = self.template.render({'data': data}, request)
        return HttpResponse(html)
