from django.shortcuts import render
from django.views.generic.base import View

from management.mixins import ManagerRequiredMixin


class IndexView(ManagerRequiredMixin, View):
    http_method_names = ('get',)

    def get(self, request):
        return render(request, 'management/managerIndex.html')
