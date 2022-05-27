from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ToDo_models.models import Task
from . import serializers


class UserTaskForTodayAPIView(APIView):
    """"Класс позволяющий получать свои задачи на сегодня/менять их"""
    def get(self, request: Request):
        objects = Task.objects.filter(authors__username=request.user)
        serializer = serializers.TaskSerializer(
            instance=objects,
            many=True,
        )
        return Response(serializer.data)

    # def put(self, request: Request):
    #     request_data_serializer = serializers.TaskSerializer(data=request.data)
    #
    #     if not request_data_serializer.is_valid():
    #         return Response(
    #             request_data_serializer.errors,
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #
    #     request_data_serializer.save(authors__username=request.user) #????
    #     return Response(
    #         request_data_serializer.data,
    #         status=status.HTTP_201_CREATED
    #     )


class PublicTaskListAPIView(APIView):
    """Класс позволяющий зарегестрированным пользователям получить доступ к публичным задачам других пользователей
    и комментировать их"""
    ...
