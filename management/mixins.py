from auth.mixins import LoginRequiredMixin
from management.models import Manager


class ManagerRequiredMixin(LoginRequiredMixin):

    def test_func(self):
        if super().test_func():
            return self.request.user.get_job().TITLE == Manager.TITLE
        return None
