from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Дата создания'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Метка")
        verbose_name_plural = _("Метки")
