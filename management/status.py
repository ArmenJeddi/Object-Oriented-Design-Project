from management.models import Manager, Employee


class ManagerRequired:

    def test(self, view):
        if view.request.user:
            return view.request.user.get_job().get_title() == Manager.get_title()
        return False


class EvaluatorRequired:

    def test(self, view):
        if view.request.user:
            return view.request.user.get_job_title() == Employee.get_title() and view.request.user.get_job().is_evaluator()
        return False


class EvaluateeRequired:

    def test(self, view):
        if view.request.user:
            return view.request.user.get_job_title() == Employee.get_title() and not view.request.user.get_job().is_evaluator()
        return False


class LoginRequired:

    def test(self, view):
        return view.request.user
        # return False
