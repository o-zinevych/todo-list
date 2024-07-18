from django.urls import path

from .views import TaskListView, TaskCreateView, TaskUpdateView

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
]
