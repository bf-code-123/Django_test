from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
    #single empty route that loads index function
]