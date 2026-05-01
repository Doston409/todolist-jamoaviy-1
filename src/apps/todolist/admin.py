from django.contrib import admin  # noqa
from apps.todolist.models import Todo
from apps.todolist.resources import TodoResources
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.


@admin.register(Todo)
class TodoModelAdmin(ImportExportActionModelAdmin):
    list_display = ['title', 'deadline']
    resource_classes = [TodoResources]