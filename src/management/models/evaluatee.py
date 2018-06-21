from django.db import models

class Evaluatee(models.Model):
    _evaluator = models.ForeignKey('Evaluator', on_delete=models.CASCADE, related_name='_evalutee_list')

    def get_evaluation_list(self):
        return self._evaluation_list
