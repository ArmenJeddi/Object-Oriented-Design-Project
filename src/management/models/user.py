from django.db import models
from django.core.exceptions import ValidationError


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
