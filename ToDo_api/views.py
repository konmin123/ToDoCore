from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ToDoCore import local_settings
from ToDo_models.models import Task
from ToDo_api import serializers, filters


class UserTaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(authors=[self.request.user])


class UserTaskUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def filter_queryset(self, queryset):
        queryset = filters.author_id_filter(queryset, author_id=self.request.user.id)
        return queryset


class UserTasksListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def filter_queryset(self, queryset):
        query_params = serializers.QueryParamsFilterSerializer(data=self.request.query_params)
        query_params.is_valid(raise_exception=True)

        queryset = filters.author_id_filter(queryset, author_id=self.request.user.id)

        status = query_params.data.get("status")
        if status:
            queryset = queryset.filter(status__in=query_params.data["status"])

        important = self.request.query_params.get("important")
        if important:
            queryset = queryset.filter(important=important)

        public = self.request.query_params.get("public")
        if public:
            queryset = queryset.filter(public=public)

        return queryset


class PublicTaskListAPIView(generics.ListAPIView):
    """Выводит публичные записи всех пользователей с комментариями"""
    queryset = Task.objects.all()
    serializer_class = serializers.TaskDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset \
            .filter(public=True) \
            .order_by("-important", "execution_time") \
            .prefetch_related("authors", "comments")


class AboutTemplateAPIView(TemplateView):
    template_name = "ToDo_api_templates/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server_version"] = local_settings.SERVER_VERSION

        return context
