from django.shortcuts import render
from django.views.generic.base import View

from auth.mixins import UserPassesTestMixin
from management.status import ManagerRequired


class IndexView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)

    def get(self, request):
        return render(request, 'management/managerIndex.html')
