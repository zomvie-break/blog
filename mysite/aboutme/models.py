from django.db import models

# Create your models here.
class Profile(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    github_url = models.URLField()
    linkedin_url = models.URLField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    