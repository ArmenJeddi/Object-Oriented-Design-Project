from django.http import HttpResponse, HttpResponseForbidden
from django.template.loader import get_template
from django.views import View

from auth.mixins import  UserPassesTestMixin
from eval.models.evaluation import EvaluationCatalog
from management.models import Employee
from management.status import LoginRequired


class EvaluationResultView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = LoginRequired()
        super().__init__(test_object, *args, **kwargs)
        self.template = get_template('viewEvaluationResult.html')

    def get(self, request, username):
        user = request.user
        if user.get_job_title() == Employee.get_title():
            if user.get_username() != username:
                return HttpResponseForbidden()
        data = EvaluationCatalog.get_instance().dump_by_username(username)
        html = self.template.render({'data': data}, request)
        return HttpResponse(html)
