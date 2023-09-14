from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.
class Weight(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)   
    mass = models.FloatField()
    created = models.DateTimeField(default=timezone.now())