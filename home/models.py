from django.db import models


class ImageData(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=50, default="")
    file = models.ImageField(upload_to='images/')


class POINT(models.Model):
    points = models.BigIntegerField()

