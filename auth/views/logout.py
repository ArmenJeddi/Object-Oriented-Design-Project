from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.conf import settings

import auth
from auth import REDIRECT_FIELD_NAME

class LogoutView(TemplateView):
    """
    Log out the user and display the 'You are logged out' message.
    """
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'auth/logged_out.html'

    def dispatch(self, request, *args, **kwargs):
        auth.logout(request)
        next_page = self.get_next_page()
        if next_page:
            # Redirect to this page until the session has been cleared.
            return HttpResponseRedirect(next_page)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        return self.get(request, *args, **kwargs)

    def get_next_page(self):
        if self.next_page is not None:
            next_page = self.next_page
        elif settings.LOGOUT_REDIRECT_URL:
            next_page = settings.LOGOUT_REDIRECT_URL
        elif (self.redirect_field_name in self.request.POST or
                self.redirect_field_name in self.request.GET):
            next_page = self.request.POST.get(
                self.redirect_field_name,
                self.request.GET.get(self.redirect_field_name)
            )
        else:
            next_page = None

        return next_page
