from django.db import models

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

    summary = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.ForeignKey('to_do_list.Status', on_delete=models.PROTECT)
    type = models.ForeignKey('to_do_list.Type', null=False, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'



