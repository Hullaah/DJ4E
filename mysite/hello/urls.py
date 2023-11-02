from django.urls import path
from .views import hello_view

app_name = "hello"
urlpatterns = [
    path("", hello_view, name="index"),
]

