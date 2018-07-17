from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from eval.mixins import EvaluateeRequiredMixin
from eval.models.evaluation import EvaluationCatalog


class EvaluationResultView(EvaluateeRequiredMixin, View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = get_template('evaluatee/evaluationResult.html')

    def get(self, request):
        evaluatee = request.user
        data = EvaluationCatalog.get_instance().dump_by_evaluatee(evaluatee)
        html = self.template.render({'data': data}, request)
        return HttpResponse(html)
