from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from rnp.decorators import singleton


class JobCatalog(models.Manager):

    def get_by_username(self, username):
        raise NotImplementedError()

    def delete_by_username(self, username):
        raise NotImplementedError()


class Job(models.Model):
    class Meta:
        abstract = True

    _user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='+', primary_key=True)

    def get_user(self):
        return self._user

    _TITLE = 'Job'
    _MAX_TITLE_LENGTH = 50
    _EMPTY_JOB_TITLE = ''

    _job_catalog_registery = {}

    @classmethod
    def get_job_catalog(cls, job_title):
        return cls._job_catalog_registery[job_title]

    @classmethod
    def set_job_catalog(cls, job_title, catalog):
        cls._job_catalog_registery[job_title] = catalog


    @classmethod
    def get_title(cls):
        return cls._TITLE

    @staticmethod
    def get_max_title_length():
        return Job._MAX_TITLE_LENGTH

    @staticmethod
    def get_empty_job_title():
        return Job._EMPTY_JOB_TITLE
    
@singleton
class UserCatalog(models.Manager):

    def get_by_username(self, username):
        user = self.get(_username=username)
        job_title = user.get_job_title()
        if job_title == Job.get_empty_job_title():
            job_object = None
        else:
            job_catalog = Job.get_job_catalog(job_title)
            job_object = job_catalog.get_by_username(user.get_username())
            
        user.set_job_object(job_object)
        return user

    def create(self, username, password, name):
        user = User(_username=username, _password=password, _name=name, _job=Job.get_empty_job_title())
        user.full_clean()
        user.save(force_insert=True)
        return user

    def delete_by_username(self, username):
        user = self.get(_username=username)
        job_title = user.get_job_title()
        if job_title:
            job_catalog = Job.get_job_catalog(job_title)
            job_catalog.delete_by_username(username)
        user.delete()

    def authenticate(self, username, password):
        try:
            return self.get(_username=username, _password=password)
        except User.DoesNotExist:
            return None

def job_validator(job_title):
    if job_title != Job.get_empty_job_title():
        try:
            Job.get_job_catalog(job_title)
        except KeyError:
            raise ValidationError('Job title is not registered.', code=User._INVALID_JOB)
        
class User(models.Model):
    
    _USERNAME_LENGTH = 10
    _PASSWORD_LENGTH = 20

    @classmethod
    def get_username_length(cls):
        return cls._USERNAME_LENGTH

    @classmethod
    def get_password_length(cls):
        return cls._PASSWORD_LENGTH

    _INVALID_USERNAME = 'invalid-username'
    _INVALID_NAME = 'invalid-name'
    _INVALID_JOB = 'invalid-job'
            
    _username = models.CharField(primary_key=True, max_length=_USERNAME_LENGTH, unique=True, validators=[RegexValidator(f'[0123456789]{{{_USERNAME_LENGTH}}}',code=_INVALID_USERNAME),])
    _password = models.CharField(max_length=_PASSWORD_LENGTH)
    _name = models.CharField(max_length=100, validators=[RegexValidator('[اآبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیءؤئإأ]*', code=_INVALID_NAME)])
    _job = models.CharField(max_length=Job.get_max_title_length(), blank=True, validators=[job_validator,])

    objects = UserCatalog.get_instance()
    
    def get_job(self):
        return self._job_object

    def set_job(self, job):
        self._job_object = job
        self._job = job.get_title()
        self.full_clean()
        self.save()

    def get_job_title(self):
        return self._job

    def set_job_object(self, job):
        self._job_object = job

    def get_username(self):
        return self._username

    def get_name(self):
        return self._name
