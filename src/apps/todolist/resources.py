from import_export import resources
from apps.todolist.models import Todo

class TodoResources(resources.ModelResource):
    class Meta:
        model = Todo