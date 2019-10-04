from django.db import models
from django.contrib.auth import get_user_model
from Base.models import BaseObject, BaseField
from NoX.fields import DropdownField


class Study(BaseObject):
    topic = models.CharField(max_length=255)


FIELD_TYPES = (
    ('text', 'Text'),
    ('numeric', 'Numeric'),
    ('dropdown', 'Dropdown'),
    ('checkbox', 'Checkbox')
)

class StudyField(BaseField):
    field_type = models.CharField(max_length=255, choices=FIELD_TYPES, default='text')
    text_value = models.CharField(max_length=255)
    numeric_value = models.DecimalField()
    dropdown_options = DropdownField()
    checkbox_value = models.BooleanField()

    



