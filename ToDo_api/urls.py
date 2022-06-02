from django.urls import path

from . import views

urlpatterns = [
    path("api/v1/newtask/", views.UserTaskCreateAPIView.as_view()),
    path("api/v1/task/<int:pk>/", views.UserTaskUpdateDestroyAPIView.as_view()),
    path("api/v1/user_tasks/", views.UserTasksListAPIView.as_view()),
    path("api/v1/public/", views.PublicTaskListAPIView.as_view()),
    path('api/v1/about/', views.AboutTemplateAPIView.as_view()),
]
