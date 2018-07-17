from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from django.views.generic import TemplateView

from eval.mixins import EvaluatorRequiredMixin, EvaluateeRequiredMixin


class EvaluateeIndexView(EvaluateeRequiredMixin, View):
    def get(self, request):
        t = get_template('evaluatee/index.html')
        username = request.user.get_username()
        html = t.render({'username': username}, request)
        return HttpResponse(html)


class EvaluatorIndexView(EvaluatorRequiredMixin, TemplateView):
    template_name = 'evaluator/index.html'
