from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
    #when visitor visits empty url, show the index path
]