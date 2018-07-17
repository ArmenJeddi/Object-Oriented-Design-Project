def singleton(cls):
    cls._instance = cls()

    def get_instance():
        return cls._instance

    cls.get_instance = get_instance

    return cls
