from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.todolist.seralizers import TodoListSeralizers,TodoCreatedSeralizers,TodoUpdateSeralizers,TodoDestroySeralizers
from apps.todolist.models import Todo


class TodoListApiView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSeralizers

class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreatedSeralizers

class TodoUpdateAPIView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoUpdateSeralizers

class TodoDestroyAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDestroySeralizers