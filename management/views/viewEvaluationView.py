from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from management.mixins import ManagerRequiredMixin
from management.models.jobs import EmployeeCatalog


class ViewEvaluationView(ManagerRequiredMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        t = get_template('management/viewEvaluation.html')
        evaluatees = EmployeeCatalog.get_instance().dump_evaluatee()
        html = t.render({'evaluatees': evaluatees}, request)
        return HttpResponse(html)
