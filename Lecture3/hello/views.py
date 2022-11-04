
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #request represents user HTTP request
    return render(request, "hello/index.html")
    #renders a whole template, not just a string

def brandon(request):
    return HttpResponse("Hello, Brandon!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    #return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
        #python dictionary
        #urls.py runs this function
        #this function takes name, renders html template, and passes name as context
        #inside of greet.html, can use the variable using django {{ }}
    })
#takes http request and name parameter that allows you to specify that person