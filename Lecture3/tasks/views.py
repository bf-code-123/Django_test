from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
        #client-side validation
        #but need server-side validation too

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        #if i look inside session (big dictionary about user) and tasks (list) not there..
        request.session["tasks"] = []
        #then create empty list of tasks
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
        #the right is the value of the variable it takes on
        #the left is the variable that django has access to
    })

def add(request):
    if request.method == "POST":
    #if user submitted form data
        form = NewTaskForm(request.POST)
        #create form variable by taking user-input data via POST
        if form.is_valid():
        #did they provide data in right format
            task = form.cleaned_data["task"]
            #give access to user submitted data
            #save task into variable
            request.session["tasks"] += [task]
            #add to list
            return HttpResponseRedirect(reverse("tasks:index"))
            #redirect to diff page after submit item
        else:
            return render(request, "tasks/add.html", {
            #give form back
                "form": form
                #send existing data back
                #calls out errors
            })

    #or if it's get
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
        #render empty form
    })