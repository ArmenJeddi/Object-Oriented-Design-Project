from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from auth.mixins import UserPassesTestMixin
from management.models.criterion import CriterionCatalog
from management.status import ManagerRequired


class ViewCriterionListView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)

    def get(self, request):
        criterion_names = CriterionCatalog.get_instance().get_names()
        t = get_template('management/viewCriteriaList.html')
        html = t.render({'criterion_names': criterion_names}, request)
        return HttpResponse(html)
