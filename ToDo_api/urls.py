from django.urls import path

from . import views

urlpatterns = [
    path('my_tasks/', views.UserTaskForTodayAPIView.as_view()),
]