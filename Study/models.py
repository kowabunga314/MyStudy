from django.db import models
from django.contrib.auth import get_user_model
from Base.models import BaseObject, BaseField


STATUSES = {
    ('planning', 'Planning'),
    ('in_progress', 'In Progress'),
    ('complete', 'Complete'),
}

FIELD_TYPES = (
    ('text', 'Text'),
    ('numeric', 'Numeric'),
    ('dropdown', 'Dropdown'),
    ('checkbox', 'Checkbox'),
)


class Study(BaseObject):
    subject = models.CharField(max_length=255)
    hypothesis = models.CharField(max_length=4096)
    status = models.CharField(max_length=32, choices=STATUSES, default='planning')


class StudyField(BaseField):
    study = models.ForeignKey(to=Study, on_delete=models.PROTECT)
    field_type = models.CharField(max_length=255, choices=FIELD_TYPES, default='text')


