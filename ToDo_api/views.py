from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ToDo_models.models import Task
from . import serializers


class UserTaskForToday(APIView):

    def get(self, request: Request):
        objects = Task.objects.filter(authors__username=request.user)
        serializer = serializers.TaskSerializer(
            instance=objects,
            many=True,
        )
        return Response(serializer.data)
