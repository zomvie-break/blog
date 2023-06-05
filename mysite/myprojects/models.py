from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    description = models.TextField(max_length=200)