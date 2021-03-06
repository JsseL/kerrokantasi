from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import BaseModel


class Label(BaseModel):
    label = models.CharField(verbose_name=_('label'), default='', max_length=200)

    class Meta:
        verbose_name = _('label')
        verbose_name_plural = _('labels')

    def __str__(self):
        return self.label
