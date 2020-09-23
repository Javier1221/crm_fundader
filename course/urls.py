from django.conf.urls import *
from . import views
from django.urls import path


urlpatterns = [
    path('', views.areas)
]