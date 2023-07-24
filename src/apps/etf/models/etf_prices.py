from django.db import models
from ...core.models.abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from .etf_isin import IsinETF


class PricesETF(TimeStampedUUIDModel):
    date = models.DateField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Date"),
        help_text=_("Date")
    )
    open = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_('Open Price'),
        help_text=_('Open Price'))
    high = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("High Price"),
        help_text=_("High Price")
    )
    low = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Low Price"),
        help_text=_("Low Price")
    )
    close = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Close Price"),
        help_text=_("Close Price")
    )
    volume = models.IntegerField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Volume"),
        help_text=_("Volume")
    )
    dividends = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Dividends"),
        help_text=_("Dividends")
    )
    splits = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Stock Splits"),
        help_text=_("Stock Splits")
    )
    capital_gains = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Capital Gains"),
        help_text=_("Capital Gains")
    )

    isin = models.ForeignKey(IsinETF, on_delete=models.CASCADE, to_field='uuid')

    class Meta:
        verbose_name = _('ETF Price')
        verbose_name_plural = _('ETFs Prices')

    def __str__(self):
        return f"{self.isin} - {self.date}: Price = {self.close})"
