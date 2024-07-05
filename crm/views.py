from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
    DetailView,
)

from crm.form import TodoForm

from .models import Todo


def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


class TodoCreateView(CreateView):
    template_name = "todo_create.html"
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")


class TodosListView(ListView):
    model = Todo
    context_object_name = "todos"
    template_name = "todo_list.html"


class TodoDeleteView(DeleteView):
    template_name = "todo_confirm_delete.html"
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    template_name = "todo_create.html"
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")


class TodoDetailView(DetailView):
    model = Todo
    context_object_name = "todo"
    template_name = "todo_detail.html"
