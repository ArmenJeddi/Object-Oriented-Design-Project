from auth.models import User
from auth import SESSION_USERNAME_FIELD

class AuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        try:
            request.user = User.objects.get(pk=request.session[SESSION_USERNAME_FIELD])
        except(User.DoesNotExist, KeyError):
            request.user = None

        return self.get_response(request)
