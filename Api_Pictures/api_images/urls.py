from django.urls import path

from . import views

urlpatterns = [
    path('get/all', views.getAllPictures, name='getAllPictures'),
    path('get/', views.getPicture, name='getPicture'),
    path('send/', views.sendPicture, name='sendPicture')
]