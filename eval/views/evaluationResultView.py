from django.http import HttpResponse, HttpResponseForbidden
from django.template.loader import get_template
from django.views import View

from auth.mixins import LoginRequiredMixin
from eval.models.evaluation import EvaluationCatalog
from management.models import Employee


class EvaluationResultView(LoginRequiredMixin, View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = get_template('viewEvaluationResult.html')

    def get(self, request, username):
        user = request.user
        if user.get_job_title() == Employee.get_title():
            if user.get_username() != username:
                return HttpResponseForbidden()
        data = EvaluationCatalog.get_instance().dump_by_username(username)
        html = self.template.render({'data': data}, request)
        return HttpResponse(html)
