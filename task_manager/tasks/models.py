from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.users.models import User

class Task(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Имя')
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('Описание')
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=_('Статус')
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='authored_tasks',
        verbose_name=_('Автор')
    )

    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executed_tasks',
        null=True,
        blank=True,
        verbose_name=_('Исполнитель')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания')
    )

    labels = models.CharField(
        max_length=255,
        unique=True
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
