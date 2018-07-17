from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from management.mixins import ManagerRequiredMixin


class ViewEvaluationView(ManagerRequiredMixin, View):
    def get(self, request):
        # evaluatee = self.get_as_evaluatee()
        # evaluation_list = evaluatee.dump_evaluation_list()
        evaluation_list = {'evaluation_list' : [
            {'name': 'name_1', 'quantitative': '200', 'qualitative': 'not so good'},
            {'name': 'name_2', 'quantitative': '300', 'qualitative': 'not so good2'},
            {'name': 'name_3', 'quantitative': '400', 'qualitative': 'not so good3'},
            {'name': 'name_4', 'quantitative': '500', 'qualitative': 'not so good4'},
            {'name': 'name_5', 'quantitative': '600', 'qualitative': 'not so good5'},
        ]}

        t = get_template('management/viewEvaluation.html')
        html = t.render(evaluation_list, request)
        return HttpResponse(html)

#   [
#   {}
#   ]