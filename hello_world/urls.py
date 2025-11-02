from django.urls import path
from . import views

app_name = "hello_world"

urlpatterns = [
    path("", views.HelloView.as_view(), name="hello"),
]
