from django.contrib import admin

from .models import Task, Comment


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'public', 'important', 'create_at',
                    'update_at', 'execution_time')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'task', 'comment')
    list_display_links = ('author', 'task')
    search_fields = ('task', 'comment')


admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)