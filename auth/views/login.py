from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import FormView

import auth
from auth import REDIRECT_FIELD_NAME
from auth import models


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=models.USERNAME_LENGTH)
    password = forms.CharField(max_length=models.PASSWORD_LENGTH)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self._user_cache = models.User.authenticate(username=username, password=password)
            if self._user_cache is None:
                raise forms.ValidationError(
                    'The credentials were invalid',
                    code='invalid_login',
                )

        return self.cleaned_data

    def get_user_id(self):
        if self._user_cache:
            return self._user_cache.id
        return None

    def get_user(self):
        return self._user_cache


class LoginView(FormView):
    """
    Display the login form and handle the login action.
    """
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'auth/login.html'
    redirect_authenticated_user = False

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

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())
