from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
app_name='addmovieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('users/',views.users,name='users'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('review/<int:movie_id>/',views.add_review,name='add_review'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]