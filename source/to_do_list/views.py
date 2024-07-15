from django.shortcuts import render, redirect
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








