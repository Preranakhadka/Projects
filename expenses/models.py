from django.db import models
from django.contrib.auth import get_user_model
import datetime
import os
import uuid


# Create your models here.
class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
