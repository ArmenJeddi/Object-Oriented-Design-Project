from ..models import User

class EmployeeCatalog:
    singleton_instance = None

    @classmethod
    def get_singleton_instance(cls):
        if cls.singleton_instance is None:
            cls.singleton_instance = EmployeeCatalog()
        return cls.singleton_instance

    def __init__(self):
        self.users = User.objects

    def getAll(self):
        return self.users.all()