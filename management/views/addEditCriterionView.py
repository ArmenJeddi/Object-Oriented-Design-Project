import json

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views import View

from management.mixins import ManagerRequiredMixin
from management.models import EvaluationCriterion
from management.models.criterion import QuantitativeOption, QualitativeOptions


class AddEditCriterionView(ManagerRequiredMixin, View):
    # model = Criterion
    # template_name = 'management/addCriterion.html'
    # fields = ['name', 'national_id']
    # success_url = '/'
    def get(self, request):
        criterion_name = request.GET.get('criterion_name')
        data = None
        if criterion_name is not None:
            data = EvaluationCriterion.dump_by_name(criterion_name)
            data = {"name": "meyar",
                    "qualitative": ["gozine3", "gozine4"],
                    "quantitative": [{"name": "gozine1", "beginning": "0", "end": "100"},
                                     {"name": "gozine2", "beginning": "100", "end": "200"}]
                    }

        t = get_template('management/addCriterion.html')
        html = t.render(data, request)
        return HttpResponse(html)

    def post(self, request):
        json_data = json.loads(request.body)
        criterion_name = json_data['name']
        qualitative_values = json_data['qualitative']
        quantitative_values = json_data['quantitative']
        EvaluationCriterion.delete_if_exists(criterion_name)
        is_quantitative = (len(quantitative_values) != 0)
        is_qualitative = (len(qualitative_values) != 0)
        criterion = EvaluationCriterion(
            _name=criterion_name,
            _is_quantitative=is_quantitative,
            _is_qualitative=is_qualitative
        )
        criterion.save()
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
        return HttpResponseRedirect('/')

# json format:
# {'name': "aaaa", 'qualitative':['aaa', 'aaa'], 'quantitative':[{'name': 'aaa', 'beginning': '1', 'end': 2}]}
