from django.urls import path

from . import views

app_name='api_img'

urlpatterns = [
    path('get/all', views.getAllPictures, name='getAllPictures'),
    path('get/', views.getPicture, name='getPicture'),
    path('send/', views.sendPicture, name='sendPicture'),
    path('error/', views.errorTest, name='errorTest'),    path('error/', views.errorTest, name='errorTest'),
]