from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from auth.mixins import LoginRequiredMixin
from management.models.criterion import CriterionCatalog


class ViewCriterionView(LoginRequiredMixin, View):
    def get(self, request):
        criterion_names = CriterionCatalog.get_instance().get_names()
        t = get_template('management/viewCriterion.html')
        html = t.render({'criterion_names':criterion_names}, request)
        return HttpResponse(html)
