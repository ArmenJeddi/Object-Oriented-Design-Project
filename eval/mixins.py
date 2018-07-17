from auth.mixins import LoginRequiredMixin


class EvaluatorRequiredMixin(LoginRequiredMixin):

    def test_func(self):
        if super().test_func():
            return self.request.user.is_evaluator()
        return None


class EvaluateeRequiredMixin(LoginRequiredMixin):

    def test_func(self):
        if super().test_func():
            return not self.request.user.is_evaluator()
        return None

