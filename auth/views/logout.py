from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic.base import View

import auth


class LogoutView(View):
    """
    Log out the user and display the 'You are logged out' message.
    """
    _next_page = None
    _redirect_field_name = auth.REDIRECT_FIELD_NAME
    _template_name = 'auth/logged_out.html'

    def get(self, request):
        auth.logout(request)
        next_page = self.get_next_page()
        return HttpResponseRedirect(next_page)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        return self.get(request)

    def get_next_page(self):
        next_page = self.request.POST.get(self._redirect_field_name, self.request.GET.get(self._redirect_field_name))
        if next_page is None:
            next_page = self._next_page
        if next_page is None:
            next_page = settings.LOGOUT_REDIRECT_URL

        return next_page
