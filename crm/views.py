from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Todo


def home(request):
    todos = Todo.objects.all()
    template = loader.get_template("home.html")

    context = {"todos": todos}

    return HttpResponse(template.render(context, request))


def todo(request):
    todos = Todo.objects.all()
    template = loader.get_template("todo/todo.html")

    context = {"todos": todos}

    return HttpResponse(template.render(context, request))


def detail_todo(request, id):
    todo = Todo.objects.get(id=id)
    template = loader.get_template("todo/detail-todo.html")

    context = {"todo": todo}

    return HttpResponse(template.render(context, request))


def login(request):
    return render(request, "login.html")
