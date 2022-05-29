from django.urls import path

from . import views

urlpatterns = [
    path('task/<int:pk>/', views.UserTaskAPIView.as_view()),
    path('newtask/', views.UserTaskAPIView.as_view()),
    path('tasks/', views.PublicTaskListAPIView.as_view()),
    path('about/', views.AboutTemplateAPIView.as_view()),
]