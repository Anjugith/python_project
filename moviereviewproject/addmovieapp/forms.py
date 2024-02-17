from django import forms
from . models import Movie,Review
class MovieForm(forms.ModelForm):

    class Meta:
        model=Movie
        fields=['title','desc','release_date','actors','category','trailer_link','poster','user_rating', 'user_review']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_rating', 'user_review']



