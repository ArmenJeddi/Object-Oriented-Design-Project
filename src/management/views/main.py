from django.views import View
from django.http import HttpResponse
from django.template.loader import get_template


class Main(View):
    def get(self, request):
        t = get_template('index.html')
        html = t.render({})
        return HttpResponse(html)
