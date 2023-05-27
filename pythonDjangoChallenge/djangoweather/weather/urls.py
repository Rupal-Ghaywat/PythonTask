from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.weather_map, name='weather_tem'),
]
