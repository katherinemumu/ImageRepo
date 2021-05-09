from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200)
    # date_uploaded = models.DateTimeField('date_uploaded')
    tag = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='', default='default.jpg')

    def __str__(self):
        return self.title + ' ' + self.image.name
