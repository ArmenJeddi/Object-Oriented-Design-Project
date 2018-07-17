from django.db import models
from auth.models import User, UserCatalog
from rnp.decorators import singleton


@singleton
class EvaluationCatalog(models.Manager):

    @staticmethod
    def evaluate_employee(evaluatee, evaluation_criterion, evaluator, qualitative_result, quantitative_result):
        evaluation = Evaluation(_evaluatee=evaluatee,
                                _evaluation_criterion=evaluation_criterion,
                                _evaluator=evaluator,
                                _qualitative_result=qualitative_result,
                                _quantitative_result=quantitative_result)
        evaluation.save()

    # def dump_all(self):
    #     employee_catalog = EmployeeCatalog.get_instance()
    #     data = []
    #     for evaluatee_job in employee_catalog.get_all_evaluatee():
    #         evaluatee = evaluatee_job.get_user()
    #         data.append(self.dump_by_evaluatee(evaluatee))
    #     return data

    def dump_by_username(self, username):
        evaluatee = UserCatalog.get_instance().get_by_username(username)
        data = []
        for evaluation in self.filter(_evaluatee=evaluatee):
            data.append(evaluation.dump())

        return {'evaluatee_name': evaluatee.get_name(), 'evaluations': data}


class Evaluation(models.Model):
    _evaluatee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    _evaluation_criterion = models.ForeignKey('management.EvaluationCriterion', on_delete=models.CASCADE)
    _evaluator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    _qualitative_result = models.CharField(max_length=20)
    _quantitative_result = models.CharField(max_length=20)

    objects = EvaluationCatalog.get_instance()

    def get_qualitative_result(self):
        return self._qualitative_result

    def get_quantitative_result(self):
        return self._quantitative_result

    def get_criterion_name(self):
        return self._evaluation_criterion.get_name()

    def dump(self):
        data = {
            # 'evaluatee_name': self._evaluatee.get_name(),
            'evaluator_name': self._evaluator.get_name(),
            'criterion': self._evaluation_criterion.get_name(),
            'qualitative_result': self._qualitative_result,
            'quantitative_result': self._quantitative_result
        }
        return data
