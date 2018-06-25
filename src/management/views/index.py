from django.views.generic import TemplateView

from management.mixins import ManagerRequiredMixin

class IndexView(ManagerRequiredMixin, TemplateView):

    template_name = 'management/managerIndex.html'
