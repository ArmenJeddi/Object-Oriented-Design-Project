from management.models import Manager, Employee


class Status:
    def test(self, view):
        raise NotImplementedError("Subclasses should implement this!")


class ManagerRequired(Status):

    def test(self, view):
        if view.request.user:
            return view.request.user.get_job().get_title() == Manager.get_title()
        return False


class EvaluatorRequired(Status):

    def test(self, view):
        if view.request.user:
            return view.request.user.get_job_title() == Employee.get_title() and view.request.user.get_job().is_evaluator()
        return False


class EvaluateeRequired(Status):

    def test(self, view):
        if view.request.user:
            return view.request.user.get_job_title() == Employee.get_title() and not view.request.user.get_job().is_evaluator()
        return False


class LoginRequired(Status):

    def test(self, view):
        return view.request.user
        # return False
