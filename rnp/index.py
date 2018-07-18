from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from auth.mixins import UserPassesTestMixin

from management.models.jobs import Manager, Employee
from management.status import LoginRequired


class IndexRedirectView(UserPassesTestMixin):

    def __init__(self, **kwargs):
        test_object = LoginRequired()
        super().__init__(test_object, **kwargs)

    def get(self, request, *args, **kwargs):
        user_job = request.user.get_job()
        if user_job.get_title() == Manager.get_title():
            return HttpResponseRedirect('/management/')
        elif user_job.get_title() == Employee.get_title():
            if user_job.is_evaluator():
                return HttpResponseRedirect('/eval/evaluatorIndex/')
            else:
                return HttpResponseRedirect('/eval/evaluateeIndex/')

        return HttpResponse('Unknown job')
