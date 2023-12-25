from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('',views.wdemo,name='wdemo'),
    #path("",views.demo,name='demo'),
    #path('add/', views.operations, name='operations'),
]
