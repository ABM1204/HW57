from django.contrib import admin
from .models import Type, Task, Status

admin.site.register(Type)
admin.site.register(Task)
admin.site.register(Status)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', 'type', 'created_at', 'updated_at')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name')
