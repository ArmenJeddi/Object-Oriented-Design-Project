from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    national_id = models.CharField(primary_key=True, max_length=10)

    def getID(self):
        return self.national_id

    def getName(self):
        return self.name
