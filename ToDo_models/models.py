from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta


class Task(models.Model):

    class Status(models.IntegerChoices):
        ACTIVE = 1, _('Активна')
        POSTPONED = 2, _('Отложена')
        COMPLETED = 3, _('Выполнена')
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    text = models.TextField(default='', verbose_name='Текст')
    status = models.IntegerField(default=Status.ACTIVE, choices=Status.choices, verbose_name='Статус')
    public = models.BooleanField(default=False, verbose_name='Публиная')
    important = models.BooleanField(default=False, verbose_name='Важная')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    execution_time = models.DateTimeField(default=(datetime.now() + timedelta(hours=24)), verbose_name='Срок выполнения')
    authors = models.ManyToManyField(User)

    def __str__(self):
        return f"Запись №{self.id}"

    class Meta:
        verbose_name = _("Задача")
        verbose_name_plural = _("Задачи")

    @property
    def authors_str(self):
        return ", ".join(str(author) for author in self.authors.all())


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment = models.TextField(default='', verbose_name='Текст')

    def __str__(self):
        return f"Комментарий №{self.id}"

    class Meta:
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")