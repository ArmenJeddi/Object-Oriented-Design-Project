from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import CreateView

from management.mixins import ManagerRequiredMixin
from ..models import Employee
from management.models.evaluator import Evaluator


class AddEvaluatorView(ManagerRequiredMixin, View):

    # POST method used for giving evaluator position to employee
    def post(self, request):
        nid = request.POST.get('username')
        employee = Evaluator.create_by_username(username=nid)
        return HttpResponseRedirect('/management/manageEvaluators/view/')
