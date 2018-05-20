from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):

    def _create_user(self, national_id, password, **extra_fields):
        if not national_id:
            raise ValueError('The given national id must be set')
        user = self.model(national_id=national_id, **extra_fields)
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)
        return user

    def create_user(self, national_id, password=None, **extra_fields):
        return self._create_user(national_id, password, **extra_fields)

    def create_superuser(self, national_id, password, **extra_fields):
        extra_fields['is_manager'] = True
        return self._create_user(national_id, password, **extra_fields)
    
class User(AbstractBaseUser):

    national_id = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)

    USERNAME_FIELD = 'national_id'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
