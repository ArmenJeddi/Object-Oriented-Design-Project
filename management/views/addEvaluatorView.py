from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import CreateView

from management.mixins import ManagerRequiredMixin
from ..models import Employee, Evaluator


class AddEvaluatorView(ManagerRequiredMixin, View):

    # POST method used for giving evaluator position to employee
    def post(self, request):
        NID = request.POST.get('national_id')
        employee = Employee.objects.get(national_id=NID)
        Evaluator.objects.create(asEmployee=employee).save()
        return HttpResponseRedirect('/evaluators')
