from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("list/", views.ProjectList.as_view(), name="list"),
    path("<uuid:pk>/", views.ProjectDetail.as_view(), name="detail"),
]
