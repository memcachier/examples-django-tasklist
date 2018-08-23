from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from mc_tasklist.models import Task
from django.core.cache import cache
import time

TASKS_KEY = "tasks.all"

def index(request):
    tasks = cache.get(TASKS_KEY)
    if not tasks:
        time.sleep(2)  # simulate a slow query.
        tasks = Task.objects.order_by("id")
        cache.set(TASKS_KEY, tasks)
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
