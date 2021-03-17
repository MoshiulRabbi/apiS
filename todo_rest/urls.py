from django.urls import path
from . import views

urlpatterns = [
    path("", views.overview, name = "overview" ),
    path("task-list/",views.tasklist, name="tasklist"),
    path("task-detail/<int:pk>/",views.taskdetail, name="taskdetail")
]
