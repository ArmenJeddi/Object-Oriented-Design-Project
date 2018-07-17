import json

from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from eval.mixins import EvaluatorRequiredMixin
from eval.models.evaluation import EvaluationCatalog
from management.models.assignment import AssignmentCatalog
from management.models.criterion import CriterionCatalog
from management.models.jobs import EmployeeCatalog


class EvaluateEmployeeView(EvaluatorRequiredMixin, View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = get_template('evaluator/evaluateEmployeeByCriterion.html')

    def get(self, request):
        evaluator = request.user
        evaluatee = AssignmentCatalog.get_instance().get_evaluatee_list(evaluator)
        criterion = CriterionCatalog.get_instance().dump_all()
        print('####################', evaluatee)
        data = {'evaluatee': evaluatee, 'criterion': criterion}
        html = self.template.render(data, request)
        return HttpResponse(html)

    def post(self, request):
        json_data = json.loads(request.body)
        for evaluatee in json_data:
            self.add_evaluation(evaluatee['username'], evaluatee['criterion'], request.user)

    @staticmethod
    def add_evaluation(evaluatee_username, criteria, evaluator):
        employee_catalog = EmployeeCatalog.get_instance()
        criterion_catalog = CriterionCatalog.get_instance()
        evaluation_catalog = EvaluationCatalog.get_instance()
        for result in criteria:
            evaluatee_job = employee_catalog.get_by_username(evaluatee_username)
            evaluatee = evaluatee_job.get_user()
            criterion = criterion_catalog.get_by_name(result['name'])
            qualitative_result = result['qualitative']
            quantitative_result = result['quantitative']
            evaluation_catalog.evaluate_employee(evaluatee, criterion, evaluator, quantitative_result,
                                                 qualitative_result)

#   data sent to template from view by GET method:
#   {
#       evaluatee:[
#           {username:12, name:ali},
#           {username:13, name:ahmad}
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
#           username: 123,
#           criterion:[
#               {
#                   name:discipline,
#                   qualitative: bad,
#                   quantitative: good
#               }
#           ]
#       }
#   ]
