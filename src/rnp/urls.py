"""rnp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management.views.addEmployee import AddEmployeeView
from management.views.viewEmployees import EmployeeListView
from management.views.editEmployee import EmployeeEditView
from management.views.evaluators import Evaluators
from management.views.main import Main
from management.views.assignEvaluatorToEmployee import AssignEvaluatorToEmployee


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', EmployeeListView.as_view()),
    path('', Main.as_view()),
    path('evaluators/', Evaluators.as_view()),
    path('assignEvaluatorToEmployee/', AssignEvaluatorToEmployee.as_view()),
    path('addEmployee/', AddEmployeeView.as_view()),
    path('editEmployee/<str:pk>/', EmployeeEditView.as_view()),
]
