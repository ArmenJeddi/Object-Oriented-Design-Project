from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views import View
from django.views.generic import CreateView

from management.models import Employee
from management.mixins import ManagerRequiredMixin
from management.models.criterion import QualitativeOptions, EvaluationCriterion


class AddRNPMethodView(ManagerRequiredMixin, View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = get_template('management/addRNP.html')
        self.select_evaluator_mode = False

    def get(self, request):
        criterion_names = EvaluationCriterion.get_names()
        html = self.template.render({
            'criterion_names': criterion_names,
        }, request
        )
        return HttpResponse(html)

    def post(self, request):
        criterion_name = request.POST.get('criterion_names')
        reward_method = request.POST.get('reward_method')
        punishment_method = request.POST.get('punishment_method')
        # criterion = EvaluationCriterion.get_by_name(criterion_name)
        EvaluationCriterion.set_reward_method(criterion_name, reward_method)
        EvaluationCriterion.set_punishment_method(criterion_name, punishment_method)
        return HttpResponseRedirect('/')
