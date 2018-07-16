from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

import auth
from auth.models import UserCatalog


class LoginView(View):
    """
    Display the login form and handle the login action.
    """
    redirect_field_name = auth.REDIRECT_FIELD_NAME
    template_name = 'auth/login.html'
    redirect_authenticated_user = False
    invalid_username_password = 1

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user is not None:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or settings.LOGIN_REDIRECT_URL

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        return redirect_to

    def get(self, request, **kwargs):
        return render(request, self.template_name, kwargs)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = UserCatalog.get_instance().authenticate(username=username, password=password)
            if user is None:
                return self.get(request, errors=[self.invalid_username_password])

        auth.login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())
