from django.db import models

class Evaluator(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='selfEvaluator')

    # TODO
    def get_evaluatee_list(self):
        pass

    # TODO
    def add_evaluatee(self):
        pass
