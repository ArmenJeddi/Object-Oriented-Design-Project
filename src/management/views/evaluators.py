from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from ..models import Employee, Evaluator


class Evaluators(View):
    def get(self, request):
        t = get_template('management/addEvaluator.html')
        employees = Employee.objects.filter(selfEvaluator__isnull=True)
        evaluators = Employee.objects.filter(selfEvaluator__isnull=False)
        html = t.render({'employees': employees, 'evaluators': evaluators}, request)
        return HttpResponse(html)

    def post(self, request):
        action = request.POST.get('action')
        NID = request.POST.get('national_id')
        employee = Employee.objects.get(national_id=NID)
        if action == 'add':
            Evaluator.objects.create(employee=employee).save()
        if action == 'remove':
            Evaluator.objects.filter(employee=employee).delete()
        return HttpResponseRedirect('/evaluators')
