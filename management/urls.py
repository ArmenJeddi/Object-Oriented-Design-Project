from django.urls import path

from eval.views.evaluateEmployeeView import EvaluateEmployeeView
from management.views.viewEvaluationView import ViewEvaluationView
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('addEmployee/', EmployeeCreateView.as_view()),
    path('manageEvaluators/add/', AddEvaluatorView.as_view()),
    path('manageEvaluators/remove/', RemoveEvaluatorView.as_view()),
    path('manageEvaluators/view/', ViewEvaluatorView.as_view()),
    path('addCriterion/', AddEditCriterionView.as_view()),
    path('editCriterion/<str:criterion_name>/', AddEditCriterionView.as_view()),
    path('viewCriterion/', ViewCriterionView.as_view()),
    path('removeCriterion/<str:criterion_name>/', RemoveCriterionView.as_view()),
    path('removeEmployee/', EmployeeDeleteView.as_view()),
    path('listEmployees/', EmployeeListView.as_view()),
    path('evaluate/', EvaluateEmployeeView.as_view()),
    path('addrnp/', AddRNPMethodView.as_view()),
    path('viewEvaluation/', ViewEvaluationView.as_view()),
    path('assignEvaluatorToEmployee/', AssignEvaluatorToEmployee.as_view())
]
