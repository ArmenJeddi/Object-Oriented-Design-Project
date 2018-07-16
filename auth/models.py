from django.db import models

USERNAME_LENGTH = 10
PASSWORD_LENGTH = 20

class Job:

    TITLE = 'Job'
    MAX_TITLE_LENGTH = 50

    _job_factory_registery = {}

    @classmethod
    def get_job_factory(cls, job):
        return cls._job_factory_registery[job]

    @classmethod
    def set_job_factory(cls, job, factory):
        cls._job_factory_registery[job.TITLE] = factory

    def __init__(self, user):
        super().__init__()

    def save(self):
        pass

    def delete(self):
        pass

class UserCatalog(models.Manager):

    def get_by_username(self, username):
        return self.get(_username=username)

    def create_user(self, username, password, name, job_title, job_data):
        user = self.Model(_username=username, _password=password, _name=name, _job=job_title, job_data=job_data)
        user.save()
        user.get_job().save()

    def delete_user(self, username):
        user = self.get(_username=username)
        user.get_job().delete()
        user.delete()
    
class User(models.Model):

    _username = models.CharField(primary_key=True, max_length=USERNAME_LENGTH, unique=True)
    _password = models.CharField(max_length=PASSWORD_LENGTH)
    _name = models.CharField(max_length=100)
    _job = models.CharField(max_length=Job.MAX_TITLE_LENGTH)

    objects = UserCatalog()

    def get_job(self):
        return self._job_object

    def __init__(self, *args, _job, job_data={}, **kwargs):
        super().__init__(*args, _job, **kwargs)
        self._job_object = Job.get_job_factory(_job)(user=self, **job_data)
        
    def get_username(self):
        return self._username

    def get_name(self):
        return self._name

    @classmethod
    def authenticate(cls, username, password):
        try:
            return cls.objects.get(_username=username, _password=password)
        except cls.DoesNotExist:
            return None
