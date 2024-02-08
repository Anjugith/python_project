from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Movie(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')


    def __str__(self):
        return self.name


# class User(models.Model):
#     user_id=models.CharField(max_length=250,blank=True)
#     def __str__(self):
#         return '{}'.format(self.user_id)