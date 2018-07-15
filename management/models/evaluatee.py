from django.db import models


class Evaluatee(models.Model):
    _evaluator = models.ForeignKey('Evaluator', on_delete=models.CASCADE, related_name='_evaluatee_list', null=True)
    _asEmployee = models.OneToOneField('Employee', on_delete=models.CASCADE, related_name='_asEvaluatee')

    def dump_evaluation_list(self):
        evaluation_list = []
        for evaluation in self._evaluation_list:
            name = evaluation.get_criterion_name()
            qualitative = evaluation.get_qualitative_result()
            quantitative = evaluation.get_quantitative_result()
            evaluation_list.append({
                'name': name,
                'qualitative': qualitative,
                'quantitative': quantitative
            })

    @classmethod
    def get_evaluatee_by_nid(cls, nid):
        return cls.objects.get(asEmployee__username=nid)

    @classmethod
    def remove_by_username(cls, username):
        cls.objects.get(_asEmployee___username=username).delete()
