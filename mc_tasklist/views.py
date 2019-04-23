from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from mc_tasklist.models import Task
from django.core.cache import cache
import time
import random
import string
from django.views.decorators.cache import cache_page
from django.utils.cache import learn_cache_key


def _hash(size=16, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def _new_tasks_key():
    return 'tasks.all.' + _hash()

TASKS_KEY = _new_tasks_key()
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
    global TASKS_KEY
    TASKS_KEY = _new_tasks_key()
    cache.delete(VIEW_KEY)
    return redirect("/")

def remove(request):
    item = Task.objects.get(id=request.POST["id"])
    if item:
        item.delete()
        global TASKS_KEY
        TASKS_KEY = _new_tasks_key()
        cache.delete(VIEW_KEY)
    return redirect("/")
