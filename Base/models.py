from django.db import models
from django.contrib.auth import get_user_model


class BaseObject(models.Model):
    name = models.CharField(max_length=255)
    owner = get_user_model()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now_add=True)


class BaseField(models.Model):
    name = models.CharField(max_length=255)
    



