from django.urls import path
from .import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("create_todo/", views.create_todo, name="create_todo"),
]
