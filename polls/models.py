from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    event = models.CharField(max_length=200)
    date = models.DateTimeField('date')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
