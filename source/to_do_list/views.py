from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, FormView
from to_do_list.forms import TaskForm
from to_do_list.models import Task

class TaskListView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by("-created_at")
        return render(request, "index.html", context={"tasks": tasks})

class TaskAddView(FormView):
    template_name = "task_add.html"
    form_class = TaskForm

    def form_valid(self, form):
        task = form.save()
        return redirect("task_detail", pk=task.pk)

class TaskDetailView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["task"] = self.task
        return context

    def get_template_names(self):
        if self.task.type:
            return ["task_detail.html"]
        else:
            return ["test_detail.html"]

class TaskUpdateView(FormView):
    template_name = "task_edit.html"
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get("pk"))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def form_valid(self, form):
        form.save()
        return redirect("task_detail", pk=self.task.pk)

def task_delete(request, pk, *args, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, "task_delete.html", context={"task": task})
    else:
        task.delete()
        return redirect("task_list")
