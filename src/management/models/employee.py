from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    national_id = models.CharField(primary_key=True, max_length=10, unique=True)
    evaluator = models.ForeignKey('Evaluator', on_delete=models.SET_NULL, related_name='selfEmployee',
                                  null=True)

    def getID(self):
        return self.national_id

    def getName(self):
        return self.name
