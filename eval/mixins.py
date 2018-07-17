from auth.mixins import LoginRequiredMixin
from management.models import Employee


class EvaluatorRequiredMixin(LoginRequiredMixin):

    def test_func(self):
        if super().test_func():
            print('wow')
            return self.request.user.get_job().TITLE == Employee.TITLE and self.request.user.get_job().is_evaluator()
        return None


class EvaluateeRequiredMixin(LoginRequiredMixin):

    def test_func(self):
        if super().test_func():
            print('qqq')
            return self.request.user.get_job().TITLE == Employee.TITLE and not self.request.user.get_job().is_evaluator()
        return None
