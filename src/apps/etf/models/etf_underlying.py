from django.db import models
from ...core.models.abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _


class Underlying(TimeStampedUUIDModel):
    underlying = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Underlying"),
        help_text=_("Underlying")
    )

    class Meta:
        verbose_name = _('Underlying')
        verbose_name_plural = _('Underlying')

    def __str__(self):
        return f"{self.underlying}"
