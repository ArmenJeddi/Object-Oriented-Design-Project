from django.views.generic import TemplateView

from eval.mixins import EvaluatorRequiredMixin, EvaluateeRequiredMixin


class EvaluateeIndexView(EvaluateeRequiredMixin, TemplateView):
    template_name = 'evaluatee/index.html'


class EvaluatorIndexView(EvaluatorRequiredMixin, TemplateView):
    template_name = 'evaluator/index.html'
