from django.urls import path
from . import views

urlpatterns = [
    path("", views.overview, name = "overview" ),
    path("task-list/",views.tasklist, name="tasklist"),
    path("task-detail/<int:pk>/",views.taskdetail, name="taskdetail"),
    path("task-create/",views.taskcreate,name= "taskcreate"),
    path("task-update/<int:pk>",views.taskupdate,name= "taskupdate"),
    path("task-delete/<int:pk>",views.taskdelete,name="taskdelete")
]
