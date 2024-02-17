from django.contrib import admin
from django.urls import path,include
from . import views
app_name='movieapp'
urlpatterns = [
    #path('',views.index,name='index.html'),

    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('search/',views.SearchResult,name='SearchResult'),
    path('edit/',views.edit_profile,name='edit_profile'),

]