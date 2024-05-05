from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class client(AbstractUser):
    clientStatus = models.BooleanField(default=True)
    contactNumber = models.CharField(max_length=200)
    startDate = models.DateField(default=None,null=True)
    endDate = models.DateField(default=None,null=True)
