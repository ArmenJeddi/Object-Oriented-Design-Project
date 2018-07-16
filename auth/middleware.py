from auth import SESSION_USERNAME_FIELD
from auth.models import User, UserCatalog


class AuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request.user = UserCatalog.get_instance().get_by_username(request.session[SESSION_USERNAME_FIELD])
        except(User.DoesNotExist, KeyError):
            request.user = None

        return self.get_response(request)
