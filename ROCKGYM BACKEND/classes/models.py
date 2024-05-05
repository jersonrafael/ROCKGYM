from django.db import models

# Create your models here.

class classes(models.Model):
    image = models.FileField(upload_to="class/", default=None)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(default=None)
    classEnd = models.DateTimeField(default=None)

class plains(models.Model):
    image = models.FileField(upload_to="plains/", default=None)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    status = models.BooleanField(default=bool) 