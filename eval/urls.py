from django.urls import path

from eval.views.evaluateEmployeeView import EvaluateEmployeeView
from eval.views.evaluationResultView import EvaluationResultView
from eval.views.index import EvaluatorIndexView, EvaluateeIndexView

urlpatterns = [
    path('evaluateeIndex/', EvaluatorIndexView.as_view()),
    path('evaluatorIndex/', EvaluateeIndexView.as_view()),
    path('evaluationResult/', EvaluationResultView.as_view()),
    path('evaluate/', EvaluateEmployeeView.as_view()),

]
