from django.db import models

USERNAME_LENGTH = 10
PASSWORD_LENGTH = 20

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=USERNAME_LENGTH)
    password = models.CharField(max_length=PASSWORD_LENGTH)
    is_manager = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    
    def get_id(self):
        return self.username

    def get_name(self):
        return self.name

    @classmethod
    def authenticate(cls, username, password):
        try:
            return cls.objects.get(username=username, password=password)
        except cls.DoesNotExist:
            return None
