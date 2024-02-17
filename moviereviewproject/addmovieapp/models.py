from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

# class Movie(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=250)
#     desc = models.TextField()
#     year = models.IntegerField()
#     img = models.ImageField(upload_to='gallery')
#
#     def __str__(self):
#         return self.name

class Movie(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    release_date = models.DateField()
    actors = models.TextField()
    category = models.CharField(max_length=100)
    trailer_link = models.URLField(max_length=255, blank=True, null=True)
    poster = models.ImageField(upload_to='movie_posters')
    user_rating = models.FloatField()
    user_review = models.TextField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
class Review(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_rating = models.FloatField()
    user_review = models.TextField()

    def __str__(self):
        return f"Review for {self.movie.title} by {self.user.username}"
# class Actor(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name



# class User(models.Model):
#     user_id=models.CharField(max_length=250,blank=True)
#     def __str__(self):
#         return '{}'.format(self.user_id)