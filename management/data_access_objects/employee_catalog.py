from auth.models import User


class EmployeeCatalog:

    def __init__(self):
        self.users = User.objects

    def getAll(self):
        return self.users.all()


EmployeeCatalog.instance = EmployeeCatalog()
