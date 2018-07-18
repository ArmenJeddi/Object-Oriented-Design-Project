from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView

from auth.mixins import UserPassesTestMixin
from management.status import EvaluateeRequired, EvaluatorRequired


class EvaluateeIndexView(UserPassesTestMixin):
    def __init__(self, *args, **kwargs):
        test_object = EvaluateeRequired()
        super().__init__(test_object, *args, **kwargs)

    def get(self, request):
        t = get_template('evaluatee/index.html')
        username = request.user.get_username()
        html = t.render({'username': username}, request)
        return HttpResponse(html)


class EvaluatorIndexView(UserPassesTestMixin):
    def __init__(self, *args, **kwargs):
        test_object = EvaluatorRequired()
        super().__init__(test_object, *args, **kwargs)

    def get(self, request):
        t = get_template('evaluator/index.html')
        html = t.render({}, request)
        return HttpResponse(html)
