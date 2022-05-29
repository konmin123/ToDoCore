from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic import TemplateView
from ToDoCore import local_settings


from ToDo_models.models import Task
from . import serializers


class AboutTemplateAPIView(TemplateView):
    template_name = "ToDo_api_templates/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server_version"] = local_settings.SERVER_VERSION

        return context


class PublicTaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset \
            .filter(public=True) \
            .order_by("-important", "execution_time") \
            .prefetch_related("authors", "comments")


class TaskAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskDetailSerializer


class TaskUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
