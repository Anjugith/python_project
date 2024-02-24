# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Movie, Comment, Review


class UserRegistrationForm(UserCreationForm):
    # Add any additional fields if needed
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','desc','release_date','actors','category','trailer_link','poster','user_rating','user_review']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_rating', 'user_review']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
