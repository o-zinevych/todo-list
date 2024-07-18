from django.urls import path

from .views import (
    TagListView,
    TagCreateView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskUpdateDoneView,
)

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "<int:pk>/update-done/",
        TaskUpdateDoneView.as_view(),
        name="task-update-done"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]
