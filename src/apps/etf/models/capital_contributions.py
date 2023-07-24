from django.db import models
from ...core.models.abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _


class CapitalContribution(TimeStampedUUIDModel):
    date = models.DateField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Date"),
        help_text=_("Date")
    )
    contribution = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Contribution"),
        help_text=_("Contribution")
    )
    currency = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Currency"),
        help_text=_("Currency")
    )

    class Meta:
        verbose_name = _('Capital Contribution')
        verbose_name_plural = _('Capital Contributions')

    def __str__(self):
        return f"{self.date} - {self.contribution} {self.currency}"
