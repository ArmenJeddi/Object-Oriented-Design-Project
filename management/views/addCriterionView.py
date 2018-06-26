from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from django.views.generic import CreateView

from management.mixins import ManagerRequiredMixin
from management.models import EvaluationCriterion
from management.models.criterion import QuantitativeOption, QualitativeOptions
import json


class AddCriterionView(ManagerRequiredMixin, View):
    # model = Criterion
    # template_name = 'management/addCriterion.html'
    # fields = ['name', 'national_id']
    # success_url = '/'
    def get(self, request):
        t = get_template('management/addCriterion.html')
        html = t.render(request)
        return HttpResponse(html)

    def post(self, request):
        json_data = json.loads(request.body)
        criterion_name = json_data['name']
        qualitative_values = json_data['qualitative']
        quantitative_values = json_data['quantitative']
        criterion = EvaluationCriterion(_name=criterion_name)
        for val in qualitative_values:
            name = val['name']
            option = QualitativeOptions(_criterion=criterion, _name=name)
            option.save()
        for val in quantitative_values:
            name = val['name']
            beginning = val['beginning']
            end = val['end']
            option = QuantitativeOption(
                _criterion=criterion, _name=name,
                _beginning=beginning, _end=end
            )
            option.save()

        criterion.save()

# json format:
# {'name': "aaaa", ['aaa', 'aaa'], [{'name': 'aaa', 'beginning': '1', 'end': 2}]}
