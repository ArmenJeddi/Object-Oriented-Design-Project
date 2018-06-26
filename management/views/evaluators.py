# from django.views import View
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template.loader import get_template
# from ..models import Employee, Evaluator
#
#
#
# class Evaluator(View):
#     # GET method used for listing all evaluatee and evaluators
#     def get(self, request):
#         t = get_template('management/addEvaluator.html')
#         evaluatee = Employee.get_all_evaluatee_employee()
#         evaluators = Employee.get_all_evaluator_employee()
#         # evaluators = Employee.objects.filter(selfEvaluator__isnull=False)
#         html = t.render({'evaluatee': evaluatee, 'evaluators': evaluators}, request)
#         return HttpResponse(html)
#
#     # POST method used for giving evaluator position to employee
#     def post(self, request):
#         # action = request.POST.get('action')
#         NID = request.POST.get('national_id')
#         employee = Employee.objects.get(national_id=NID)
#         # if action == 'add':
#         Evaluator.objects.create(asEmployee=employee).save()
#
#         # if action == 'remove':
#         #     Evaluator.objects.filter(employee=employee).delete()
#         return HttpResponseRedirect('/evaluators')
#
#     # DELETE method used for taking back evaluator position
#     def delete(self, request):
#         NID = request.POST.get('national_id')
#         employee = Employee.objects.get(national_id=NID)
#         Evaluator.objects.get(asEmployee=employee).delete()
#         return HttpResponseRedirect('/evaluators')
