from django.db import models

from django.db import models
from to_do_list.validators import summary_length, min_words

class Type(models.Model):
    name = models.CharField(max_length=100, default='Task', verbose_name='Type')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type'
        verbose_name = 'Type'
        verbose_name_plural = 'Types'


class Status(models.Model):
    name = models.CharField(max_length=100, default='new', verbose_name='Status')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'status'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Task(models.Model):
    summary = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        validators=[summary_length],
        verbose_name='Summary'
    )
    description = models.TextField(
        null=True,
        blank=True,
        validators=[min_words],
        verbose_name='Description'
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Status')
    type = models.ForeignKey(Type, null=False, on_delete=models.PROTECT, verbose_name='Type')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.summary

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'