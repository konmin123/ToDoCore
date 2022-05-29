from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from ToDoCore import local_settings


from ToDo_models.models import Task
from . import serializers


class AboutAPIView(View):
    def get(self, request):
        user = request.user
        context = {
            "server_version": local_settings.SERVER_VERSION, "user": user
        }
        return render(request, 'ToDo_api_templates/about.html', context=context)

# class MyTasksListTodayAPIView(ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = serializers.TaskDetailSerializer
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#
#         return queryset \
#             .filter(public=True) \
#             .order_by("important", "-create_at") \
#             .prefetch_related("authors", "comments")


class PublicTaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset \
            .filter(public=True) \
            .order_by("-important", "execution_time") \
            .prefetch_related("authors", "comments")


class UserTaskAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
