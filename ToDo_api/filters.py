from django.db.models.query import QuerySet


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


