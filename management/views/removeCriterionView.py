from django.http import HttpResponseRedirect
from django.views import View

from auth.mixins import UserPassesTestMixin
from management.models.criterion import CriterionCatalog
from management.status import ManagerRequired


class RemoveCriterionView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)

    def get(self, request, criterion_name):
        CriterionCatalog.get_instance().delete_if_exists(criterion_name)
        return HttpResponseRedirect('/management/viewCriterion/')
