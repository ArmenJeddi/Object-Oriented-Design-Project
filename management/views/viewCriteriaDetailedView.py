from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from auth.mixins import UserPassesTestMixin
from management.models.criterion import CriterionCatalog
from management.status import  LoginRequired


class ViewCriterionDetailedView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = LoginRequired()
        super().__init__(test_object, *args, **kwargs)

    def get(self, request):
        criteria = CriterionCatalog.get_instance().dump_all()
        t = get_template('management/viewCriteriaDetailed.html')
        html = t.render({'criteria': criteria}, request)
        return HttpResponse(html)
