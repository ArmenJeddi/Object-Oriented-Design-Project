REDIRECT_FIELD_NAME = 'next'
SESSION_USERNAME_FIELD = '_username'

def login(request, user):
    request.session[SESSION_USERNAME_FIELD] = user.get_id()

def logout(request):
    request.session.flush()
