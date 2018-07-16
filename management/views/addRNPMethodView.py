from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views import View
from django.views.generic import CreateView

from management.models import Employee
from management.mixins import ManagerRequiredMixin
from management.models.criterion import QualitativeOptions, EvaluationCriterion, CriterionCatalog


class AddRNPMethodView(ManagerRequiredMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = get_template('management/addRNP.html')
        self.select_evaluator_mode = False

    def get(self, request):
        criteria = CriterionCatalog.get_instance().get_names_and_rnp()
        html = self.template.render({
            'criteria': criteria,
        }, request
        )
        return HttpResponse(html)

    def post(self, request):
        criterion_catalog = CriterionCatalog.get_instance()
        criterion_name = request.POST.get('criterion_names')
        reward_method = request.POST.get('reward_method')
        punishment_method = request.POST.get('punishment_method')
        # criterion = EvaluationCriterion.get_by_name(criterion_name)
        criterion_catalog.set_reward_method(criterion_name, reward_method)
        criterion_catalog.set_punishment_method(criterion_name, punishment_method)
        return HttpResponseRedirect('/')