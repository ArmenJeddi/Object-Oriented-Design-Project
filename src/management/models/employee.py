from django.db import models
from . import User

class Employee(models.Model):
    name = models.CharField(max_length=100)
    ID = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def getID(self):
        return self.ID

    def getName(self):
        return self.name
