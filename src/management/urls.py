from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('addEmployee/', AddEmployeeView.as_view()),
    path('manageEvaluators/', ManageEvaluatorsView.as_view()),
    path('addEvaluator/<str:username>/', AddEvaluatorView.as_view()),
    path('deleteEvaluator/<str:username>/', DeleteEvaluatorView.as_view()),
    path('listEmployees/', EmployeeListView.as_view()),
]
