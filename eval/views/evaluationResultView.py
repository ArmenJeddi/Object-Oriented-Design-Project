from django.http import HttpResponse, HttpResponseForbidden
from django.template.loader import get_template
from django.views import View

from auth.mixins import  UserPassesTestMixin
from eval.models.evaluation import EvaluationCatalog
from management.models import Employee, Manager
from management.status import LoginRequired


class EvaluationResultView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = LoginRequired()
        super().__init__(test_object, *args, **kwargs)
        self.user_template = get_template('viewEvaluationResult.html')
        self.manager_template = get_template('viewEvaluationResultManager.html')

    def get(self, request, username):
        user = request.user
        current_username = request.user.get_username()
        if user.get_job_title() == Employee.get_title():
            if user.get_username() != username:
                return HttpResponseForbidden()
            data = EvaluationCatalog.get_instance().dump_by_username(username)
            print(data)
            html = self.user_template.render({'data': data, 'username': current_username}, request)
        elif user.get_job_title() == Manager.get_title():
            data = EvaluationCatalog.get_instance().dump_by_username(username)
            print(data)
            html = self.manager_template.render({'data': data, 'username': current_username}, request)
        else:
            return HttpResponseForbidden()

        return HttpResponse(html)
