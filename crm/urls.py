from django.urls import path

from .views import (
    TodoCreateView,
    TodoDeleteView,
    TodoDetailView,
    TodoUpdateView,
    TodosListView,
)
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todo/", TodosListView.as_view(), name="todo_list"),
    path("todo/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todo/delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("todo/update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("todo/<int:pk>", TodoDetailView.as_view(), name="todo_detail"),
]
