from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="index"),
    path('detail/<str:name>', views.detail ,name="detail"),
    path('userform', views.userform, name="userform"),
    path('map', views.map, name="map" ),
]