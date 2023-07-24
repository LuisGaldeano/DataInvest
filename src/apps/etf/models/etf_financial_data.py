from django.db import models
from ...core.models.abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from .etf_isin import IsinETF


class FinancialDataETF(TimeStampedUUIDModel):
    date = models.DateField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Date"),
        help_text=_("Date")
    )
    fiftyTwoWeekLow = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Fifty Two Week Low"),
        help_text=_("Fifty Two Week Low")
    )
    fiftyTwoWeekHigh = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Fifty Two Week High"),
        help_text=_("Fifty Two Week High")
    )
    fiftyDayAverage = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Fifty Day Average"),
        help_text=_("Fifty Day Average")
    )
    twoHundredDayAverage = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Two Hundred Day Average"),
        help_text=_("Two Hundred Day Average")
    )
    ytdReturn = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("YTD Return"),
        help_text=_("YTD Return")
    )
    beta3Year = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Beta 3 Year"),
        help_text=_("Beta 3 Year")
    )
    threeYearAverageReturn = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Three Year Average Return"),
        help_text=_("Three Year Average Return")
    )
    fiveYearAverageReturn = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Five Year Average Return"),
        help_text=_("Five Year Average Return")
    )

    isin = models.ForeignKey(IsinETF, on_delete=models.CASCADE, to_field='uuid')

    class Meta:
        verbose_name = _('Financial Data ETF')
        verbose_name_plural = _('Financial Data ETFs')

    def __str__(self):
        return f"{self.date} - {self.isin}: {self.totalAssets}"
