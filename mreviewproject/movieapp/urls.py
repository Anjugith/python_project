# urls.py
from django.urls import path
from . import views
app_name = 'movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('search/',views.SearchResult,name='SearchResult'),
    path('users/',views.users,name='users'),
    path('update/<int:id>/', views.update, name='update'),
    path('edit/',views.edit_profile,name='edit_profile'),
    path('add/',views.add_movie,name='add_movie'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('review/<int:movie_id>/',views.add_review,name='add_review'),
    # path('category/<int:category_id>/', views.category_movies, name='category_movies'),
    # path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    # path('movies/', views.movie_list, name='movie_list'),
    # path('movie/<int:movie_id>/add_comment/', views.add_comment, name='add_comment'),
    # Add other URLs as needed
]
