from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="list-tasks"),
    path("create/", views.create_task, name="create-tasks"),
    path("delete/", views.delete_task, name="delete-tasks"),
]
