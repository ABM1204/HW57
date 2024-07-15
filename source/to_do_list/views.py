from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from to_do_list.forms import TaskForm
from to_do_list.models import Task


class TaskListView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks': tasks})



class TaskAddView(View):
    def dispatch(self, request, *args, **kwargs):
        print(request.POST)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task_add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                type=form.cleaned_data['type'],
                status=form.cleaned_data['status']
            )
            return redirect('task_list')
        return render(request, 'task_add.html', {'form': form})


class TaskDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        template_name = "task_detail.html" if task.type else "test_detail.html"
        return render(request, template_name, {'task': task})

    def task_edit(request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        if request.method == "GET":
            form = TaskForm(initial={
                "summary": task.summary,
                "description": task.description,
                "type": task.type,
                "status": task.status,
            })
            return render(request, "task_edit.html", context={"form": form, "task": task})
        else:
            form = TaskForm(data=request.POST)
            if form.is_valid():
                task.summary = form.cleaned_data['summary']
                task.description = form.cleaned_data['description']
                task.type = form.cleaned_data['type']
                task.status = form.cleaned_data['status']
                task.save()
                return redirect("task_detail", pk=task.pk)
            else:
                return render(request, "task_edit.html", context={"form": form, "task": task})

    def task_delete(request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        if request.method == "GET":
            return render(request, "task_delete.html", context={"task": task})
        else:
            task.delete()
            return redirect("task_list")











