from django.db import models

# Create your models here.

class Image(models.Model):
    date_uploaded = models.DateTimeField('date_uploaded')
    tags = models.CharField(max_length=200)
