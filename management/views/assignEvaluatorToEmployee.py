from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template

from management.mixins import ManagerRequiredMixin
from ..models import Employee, Evaluator


class AssignEvaluatorToEmployee(ManagerRequiredMixin, View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = get_template('management/assignEvaluatorToEmployee.html')
        self.select_evaluator_mode = False

    def get(self, request):
        evaluatee = Employee.objects.filter(selfEvaluator__isnull=True)
        html = self.template.render({
            'persons': evaluatee,
            'select_evaluator_mode': self.select_evaluator_mode
        }, request)
        return HttpResponse(html)

    def post(self, request):
        mode = request.POST.get('mode')
        NID = request.POST.get('national_id')
        if mode == 'evaluatee':
            evaluators = Employee.objects.filter(selfEvaluator__isnull=False)
            self.select_evaluator_mode = True
            html = self.template.render({
                'persons': evaluators,
                'select_evaluator_mode': self.select_evaluator_mode,
                'evaluatee_NID': NID
            }, request)
            response = HttpResponse(html)
        if mode == 'evaluator':
            evaluatee_NID = request.POST.get('evaluatee_NID')
            evaluator_NID = request.POST.get('national_id')
            evaluator = Evaluator.get_evaluator(evaluator_NID)
            evaluator.add_evaluatee(evaluatee_NID)
            response = HttpResponseRedirect('/')
        return response
