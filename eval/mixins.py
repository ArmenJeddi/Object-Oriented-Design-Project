from auth.mixins import LoginRequiredMixin
from management.models import Evaluator


class EvaluatorRequiredMixin(LoginRequiredMixin):

    def test_func(self):
        if super().test_func():
            return Evaluator.is_evaluator(self.request.user)
        return None

    def get_evaluator(self):
        return Evaluator.get_by_username(self.request.user)
