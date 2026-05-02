from rest_framework.serializers import ModelSerializer
from apps.todolist.models import Todo

class TodoListSeralizers(ModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"


class TodoCreatedSeralizers(ModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"


class TodoUpdateSeralizers(ModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"


class TodoDestroySeralizers(ModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"