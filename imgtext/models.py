from django.db import models

# Create your models here.
class imgFile(models.Model):
    imgs = models.FileField()
    