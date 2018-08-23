from django.views.decorators.cache import cache_page
from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from mc_tasklist.models import Task
from django.core.cache import cache
from django.utils.cache import learn_cache_key
import time

TASKS_KEY = "tasks.all"
VIEW_KEY = ""

@cache_page(None)
def index(request):
    tasks = cache.get(TASKS_KEY)
    if not tasks:
        time.sleep(2)  # simulate a slow query.
        tasks = Task.objects.order_by("id")
        cache.set(TASKS_KEY, tasks)
    c = {'tasks': tasks}
    c.update(csrf(request))
    response = render_to_response('index.html', c)
    global VIEW_KEY
    VIEW_KEY = learn_cache_key(request, response)
    return response

def add(request):
    item = Task(name=request.POST["name"])
    item.save()
    cache.set(TASKS_KEY, Task.objects.order_by("id"))
    cache.delete(VIEW_KEY)
    return redirect("/")

def remove(request):
    item = Task.objects.get(id=request.POST["id"])
    if item:
        item.delete()
        cache.set(TASKS_KEY, Task.objects.order_by("id"))
        cache.delete(VIEW_KEY)
    return redirect("/")
