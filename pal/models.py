from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)
    currently_active = models.BooleanField()
    associated_with = models.ForeignKey(User, on_delete=models.CASCADE)
