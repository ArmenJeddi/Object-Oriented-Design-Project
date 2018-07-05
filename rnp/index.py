from django.views.generic import View
from django.shortcuts import redirect

from auth.mixins import LoginRequiredMixin

class IndexRedirectView(LoginRequiredMixin):

    http_method_names = ['get']
    
    def get(self, request, *args, **kwargs):
        if request.user.get_is_manager():
            return redirect('/management/')
        else:
            return redirect('/eval/')
