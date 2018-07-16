import json

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views import View

from management.mixins import ManagerRequiredMixin
from management.models import EvaluationCriterion
from management.models.criterion import QuantitativeOption, QualitativeOptions, CriterionCatalog


class AddEditCriterionView(ManagerRequiredMixin, View):
    def get(self, request, criterion_name=None):
        data = None
        if criterion_name is not None:
            data = CriterionCatalog.get_instance().dump_by_name(criterion_name)

        t = get_template('management/addCriterion.html')
        html = t.render(data, request)
        return HttpResponse(html)

    def post(self, request):
        json_data = json.loads(request.body)
        criterion_name = json_data['name']
        qualitative_values = json_data['qualitative']
        quantitative_values = json_data['quantitative']
        print(qualitative_values)
        print(quantitative_values)
        CriterionCatalog.get_instance().delete_if_exists(criterion_name)
        is_quantitative = (len(quantitative_values) != 0)
        is_qualitative = (len(qualitative_values) != 0)
        criterion = EvaluationCriterion(
            _name=criterion_name,
            _is_quantitative=is_quantitative,
            _is_qualitative=is_qualitative
        )
        criterion.save()
        for val in qualitative_values:
            name = val
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
