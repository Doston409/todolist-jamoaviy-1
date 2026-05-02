from django.urls import path
from apps.todolist.views import TodoListApiView,TodoDestroyAPIView,TodoCreateAPIView,TodoUpdateAPIView



urlpatterns = [
    path("list/",TodoListApiView.as_view()),
    path("create/",TodoCreateAPIView.as_view()),
    path("update/<int:pk/",TodoUpdateAPIView.as_view()),
    path("delete/<int:pk/",TodoDestroyAPIView.as_view()),
]
