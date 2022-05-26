from datetime import datetime

from rest_framework import serializers

from ToDo_models.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
