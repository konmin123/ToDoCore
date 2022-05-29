from django.urls import path

from . import views

urlpatterns = [
    path('newtask/', views.TaskAPIView.as_view()),
    path('task/<int:pk>/', views.TaskUpdateDestroyAPIView.as_view()),
    path('tasks/', views.PublicTaskListAPIView.as_view()),
    path('about/', views.AboutTemplateAPIView.as_view()),
]