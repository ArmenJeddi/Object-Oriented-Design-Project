from django.views.generic import View
from django.shortcuts import redirect

from auth.mixins import LoginRequiredMixin
from management.models import Manager


class IndexRedirectView(LoginRequiredMixin):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        if request.user.get_job().TITLE == Manager.TITLE:
            return redirect('/management/')
        else:
            return redirect('/eval/')
