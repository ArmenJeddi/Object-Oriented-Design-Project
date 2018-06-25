from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import redirect

from management.models import Employee, Evaluator

from management.mixins import ManagerRequiredMixin

class ManageEvaluatorsView(ManagerRequiredMixin, TemplateView):

    template_name = 'management/addEvaluator.html'

    def get_context_data(self, **kwargs):
        kwargs['evaluators'] = Employee.objects.filter(asEvaluator__isnull=False)
        kwargs['employees'] = Employee.objects.filter(asEvaluator__isnull=True)

class DeleteEvaluatorView(ManagerRequiredMixin, SingleObjectMixin):

    http_method_names = ['post']
    model = Employee
    pk_url_kwarg = 'username'

    def post(self, request, *args, **kwargs):
        employee = super().get_object()
        employee.asEvaluator.delete()
        employee.asEvaluator = None
        employee.save()
        return redirect('/management/manageEvaluators/')

class AddEvaluatorView(ManagerRequiredMixin, SingleObjectMixin):

    http_method_names = ['post']
    model = Employee
    pk_url_kwarg = 'username'

    def post(self, request, *args, **kwargs):
        employee = super().get_object()
        if employee.asEvaluatee:
            employee.asEvaluatee.delete()
            employee.asEvaluatee = None
        evaluator = Evaluator.objects.create()
        employee.asEvaluator = evaluator
        employee.save()
        return redirect('/management/manageEvaluators/')
