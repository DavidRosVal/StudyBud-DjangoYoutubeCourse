""" This urls.py is for the specific app (base), the other one in studybud is for the project in general """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"),
]
