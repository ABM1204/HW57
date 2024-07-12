# forms.py
from django import forms
from to_do_list.models import Task, Type, Status

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'type', 'status']
