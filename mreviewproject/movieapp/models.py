# models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

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

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
class Review(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_rating = models.FloatField()
    user_review = models.TextField()

    def __str__(self):
        return f"Review for {self.movie.title} by {self.user.username}"