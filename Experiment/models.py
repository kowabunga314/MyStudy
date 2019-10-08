from django.db import models
from Base.models import BaseObject, BaseField
from Study.models import Study, StudyField
from NoX.fields import DropdownField


class Experiment(models.Model):
    study = models.ForeignKey(to=Study, to_field='id', on_delete=models.PROTECT)


class ExperimentField(BaseField):
    study_field = models.ForeignKey(to=StudyField, on_delete=models.PROTECT)
    experiment = models.ForeignKey(to=Experiment, on_delete=models.PROTECT)
    text_value = models.CharField(max_length=255, default=None)
    numeric_value = models.DecimalField(decimal_places=15, max_digits=15, default=None)
    dropdown_options = DropdownField(default=None)
    checkbox_value = models.BooleanField(default=False)

