from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView


from ToDo_models.models import Task
from . import serializers


class MyTasksListTodayAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset \
            .filter(public=True) \
            .order_by("important", "-create_at") \
            .prefetch_related("authors", "comment_set")


class PublicTaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset \
            .filter(public=True) \
            .order_by("important", "-create_at") \
            .prefetch_related("authors", "comment_set")


class UserTaskAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
