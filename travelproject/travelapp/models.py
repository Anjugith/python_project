from django.db import models


# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name
class Workers(models.Model):
    wname=models.CharField(max_length=250)
    pic=models.ImageField(upload_to='pics')
    disc=models.TextField()
    def __str__(self):
        return self.wname