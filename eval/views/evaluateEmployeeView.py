from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template
from django.views import View
from django.views.generic import CreateView

from eval.mixins import EvaluatorRequiredMixin
from management.mixins import ManagerRequiredMixin
from management.models import EvaluationCriterion
from management.models.evaluator import Evaluator
from management.models.evaluatee import  Evaluatee
from management.models.criterion import QuantitativeOption, QualitativeOptions
import json


class EvaluateEmployeeView(EvaluatorRequiredMixin, View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = get_template('management/evaluateEmployeeByCriterion.html')

    def get(self, request):
        evaluator = self.get_evaluator()
        evaluatee = evaluator.dump_evaluatee_list()
        criterion = EvaluationCriterion.dump_all()
        data = {'evaluatee': evaluatee, 'criterion': criterion}
        html = self.template.render(data, request)
        return HttpResponse(html)

    def post(self, request):
        json_data = json.loads(request.body)
        for evaluatee in json_data:
            self.add_evaluation(evaluatee['id'], evaluatee['criterion'])

    def add_evaluation(self, evaluatee_id, criteria):
        for result in criteria:
            evaluatee = Evaluatee.get_evaluatee_by_nid(evaluatee_id)
            criterion = EvaluationCriterion.get_by_name(result['name'])
            qualitative_result = result['qualitative']
            quantitative_result = result['quantitative']
            evaluator = self.get_evaluator()
            evaluator.evaluate_employee(evaluatee, criterion, quantitative_result, qualitative_result)

#   data sent to template from view by GET method:
#   {
#       evaluatee:[
#           {id:12, name:ali},
#           {id:13, name:ahmad}
#       ],
#       criterion:[
#           {
#               name:discipline,
#               qualitative:[
#                   good,
#                   bad
#               ],
#               quantitative:[
#                   {
#                       name:good,
#                       beginning: 12 ----> only int value
#                       end: 15
#                   }
#               ]
#           }
#       ]
#    }

#   data received by view from template by POST method:
#   [
#       {
#           id: 123,
#           criterion:[
#               {
#                   name:discipline,
#                   qualitative: bad,
#                   quantitative: good
#               }
#           ]
#       }
#   ]
