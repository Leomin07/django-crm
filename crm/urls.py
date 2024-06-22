from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todo", views.todo, name="todo"),
    path("todo/<int:id>", views.detail_todo, name="detail"),
    path("login", views.login, name="login"),
]
