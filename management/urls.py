from django.urls import path

from management.views.addCriterionView import CriterionView

from management.views.addEditCriterionView import AddEditCriterionView
from management.views.viewEvaluatorView import ViewEvaluatorView
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('addEmployee/', AddEmployeeView.as_view()),
    path('manageEvaluators/add', AddEvaluatorView.as_view()),
    path('manageEvaluators/remove', RemoveEvaluatorView.as_view()),
    path('manageEvaluators/view', ViewEvaluatorView.as_view()),
    path('addCriterion', AddEditCriterionView.as_view()),
    path('editCriterion/<str:criterion_name>/', AddEditCriterionView.as_view()),
    # path('addEvaluator/<str:username>/', AddEvaluatorView.as_view()),
    # path('deleteEvaluator/<str:username>/', DeleteEvaluatorView.as_view()),
    path('listEmployees/', EmployeeListView.as_view()),
]