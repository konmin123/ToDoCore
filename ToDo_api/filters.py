from django.db.models.query import QuerySet
from django_filters import rest_framework as filters

from ToDo_models.models import Task


class TaskFilter(filters.FilterSet):
    year = filters.NumberFilter(
        field_name="create_at",
        lookup_expr="year",
        help_text="Год статьи"
    )

    class Meta:
        model = Task
        fields = ['title', 'authors', 'year',
                  'status', 'important', 'public']


def author_id_filter(queryset: QuerySet, author_id):
    return queryset.filter(authors=author_id)


def important_filter(queryset):
    return queryset.filter(important=True)


def public_filter(self, queryset):
    return queryset.filter(public=True)


def activity_filter(queryset):
    return queryset.filter(status=1)


def completed_task_filter(self, queryset):
    return queryset.filter(status=3)


