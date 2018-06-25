from auth.mixins import LoginRequiredMixin


class ManagerRequiredMixin(LoginRequiredMixin):

    def test_func(self):
        if super().test_func():
            return self.request.user.is_manager
        return None
