from django.urls import path

from . import views

urlpatterns = [
    path('my_tasks/', views.UserTaskForToday.as_view()),
]