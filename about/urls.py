from django.urls import path
from . import views

app_name = "about"

urlpatterns = [
    path("", views.AboutList.as_view(), name="list"),
]
