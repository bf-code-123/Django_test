from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #when visitor visits empty url, show the index path
    path("brandon", views.brandon, name="brandon"),
    path("david", views.david, name="david"),
    path("<str:name>", views.greet, name="greet")
    #this route can be any string with variable name name. call greet function
    #pass in variable name as parameter
]