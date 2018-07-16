from django.db import models

from rnp.decorators import singleton

USERNAME_LENGTH = 10
PASSWORD_LENGTH = 20


class JobCatalog(models.Manager):

    def get_by_username(self, username):
        raise NotImplementedError()

    def delete_by_username(self, username):
        raise NotImplementedError()

    def create(self, user, *args, **kwargs):
        raise NotImplementedError()


class Job(models.Model):
    class Meta:
        abstract = True

    _user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='+')

    def get_user(self):
        return self._user

    TITLE = 'Job'
    MAX_TITLE_LENGTH = 50

    _job_catalog_registery = {}

    @classmethod
    def get_job_catalog(cls, job_title):
        return cls._job_catalog_registery[job_title]

    @classmethod
    def set_job_catalog(cls, job_title, catalog):
        cls._job_catalog_registery[job_title] = catalog


@singleton
class UserCatalog(models.Manager):

    def get_by_username(self, username):
        user = self.get(_username=username)
        job_catalog = Job.get_job_catalog(user._get_job_title())
        job_object = job_catalog.get_by_username(user.get_username())
        user._set_job_object(job_object)
        return user

    def create(self, username, password, name, job_title, job_data=None):
        user = User(_username=username, _password=password, _name=name, _job=job_title)
        user.save()
        job_catalog = Job.get_job_catalog(job_title)
        if job_data is None:
            job_data = {}
        job_object = job_catalog.create(user=user, **job_data)
        user._set_job_object(job_object)
        return user

    def delete(self, username):
        user = self.get(_username=username)
        job_catalog = Job.get_job_catalog(user._get_job_title())
        job_catalog.delete_by_username(username)
        user.delete()


class User(models.Model):
    _username = models.CharField(primary_key=True, max_length=USERNAME_LENGTH, unique=True)
    _password = models.CharField(max_length=PASSWORD_LENGTH)
    _name = models.CharField(max_length=100)
    _job = models.CharField(max_length=Job.MAX_TITLE_LENGTH)

    objects = UserCatalog.get_instance()

    def get_job(self):
        return self._job_object

    def _set_job_object(self, job):
        self._job_object = job

    def _get_job_title(self):
        return self._job

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
