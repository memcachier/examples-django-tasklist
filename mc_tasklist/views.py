from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from mc_tasklist.models import Task

def index(request):
    tasks = Task.objects.order_by("id")
    c = {'tasks': tasks}
    c.update(csrf(request))
    return render_to_response('index.html', c)

def add(request):
    item = Task(name=request.POST["name"])
    item.save()
    return redirect("/")

def remove(request):
    item = Task.objects.get(id=request.POST["id"])
    if item:
        item.delete()
    return redirect("/")
