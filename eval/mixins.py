from auth.mixins import LoginRequiredMixin
from management.models import Employee


class EvaluatorRequiredMixin(LoginRequiredMixin):

    def test_func(self):
        if super().test_func():
            return self.request.user.get_job_title() == Employee.get_title() and self.request.user.get_job().is_evaluator()
        return None


class EvaluateeRequiredMixin(LoginRequiredMixin):

    def test_func(self):
        if super().test_func():
            return self.request.user.get_job_title() == Employee.get_title() and not self.request.user.get_job().is_evaluator()
        return None
