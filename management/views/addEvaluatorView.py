from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import CreateView

from management.mixins import ManagerRequiredMixin
from management.models import Employee


class AddEvaluatorView(ManagerRequiredMixin, View):

    # POST method used for giving evaluator position to employee
    def post(self, request):
        username = request.POST.get('username')
        Employee.set_as_evaluator(username)
        return HttpResponseRedirect('/management/manageEvaluators/view/')
