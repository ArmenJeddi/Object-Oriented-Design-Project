from django.db import models

from eval.models.evaluation import Evaluation


class Evaluator(models.Model):
    _asEmployee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='asEvaluator')

    def evaluate_employee(self, evaluatee, evaluation_criterion, quantitative_result, qualitative_result):
        return Evaluation(
            evaluation_criterion=evaluation_criterion,
            quantitative_result=quantitative_result,
            qualitative_result=qualitative_result,
            evaluator=self,
            evaluatee=evaluatee)

    def add_evaluatee(self, evaluatee):
        evaluatee._evaluator = self

    def dump_evaluatee_list(self):
        dump_data = []
        for evaluatee in self._evaluatee_list:
            dump_data.append({
                'id': evaluatee.asEmployee_id,
                'name': evaluatee.asEmployee_name,
            })
        return dump_data

    @classmethod
    def find(cls, evaluator_nid):
        return cls.objects.get(asEmployee__username=evaluator_nid)

    @classmethod
    def is_evaluator(cls, user):
        return cls.objects.filter(_asEmployee_id__username=user.get_id()).count() == 1

    @classmethod
    def delete_by_nid(cls, nid):
        cls.objects.get(_asEmployee___username=nid).delete()
