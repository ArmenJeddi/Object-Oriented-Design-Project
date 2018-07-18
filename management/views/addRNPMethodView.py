import json

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views import View

from auth.mixins import UserPassesTestMixin
from management.models.criterion import CriterionCatalog
from management.status import ManagerRequired


class AddRNPMethodView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)
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
        data = json.loads(request.body)
        criterion_catalog = CriterionCatalog.get_instance()
        for json_data in data:
            criterion_name = json_data['name']
            reward_method = json_data['reward']
            punishment_method = json_data['punishment']
            criterion = criterion_catalog.get_by_name(criterion_name)
            criterion.set_reward(reward_method)
            criterion.set_punishment(punishment_method)
        return HttpResponseRedirect('/')
