from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)
    currently_active = models.BooleanField()
    associated_with = models.ForeignKey(User, on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=255)
    associated_group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Topic(models.Model):
    name = models.CharField(max_length=255)
    associated_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class TopicRevision(models.Model):
    associated_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)