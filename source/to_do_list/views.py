from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from to_do_list.models import Task


class TaskListView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks': tasks})


