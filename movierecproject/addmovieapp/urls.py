from . import views
from django.urls import path
app_name='addmovieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('users/<int:id>',views.users,name='users'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),

]