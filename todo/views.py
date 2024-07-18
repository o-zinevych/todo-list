from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateDoneView(generic.RedirectView):
    pattern_name = "todo:task-list"

    def get_redirect_url(self, *args, **kwargs):
        task = Task.objects.get(id=kwargs["pk"])
        task.is_done = False if task.is_done else True
        task.save()
        return super().get_redirect_url()
