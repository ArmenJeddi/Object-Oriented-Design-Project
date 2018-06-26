from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import DeleteView

from ..models import Employee, Evaluator



class RemoveEvaluatorView(DeleteView):

    # DELETE method used for taking back evaluator position
    def post(self, request):
        NID = request.POST.get('national_id')
        employee = Employee.objects.get(national_id=NID)
        Evaluator.objects.get(asEmployee=employee).delete()
        return HttpResponseRedirect('/evaluators')
