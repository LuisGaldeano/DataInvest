from django.db import models
from ...core.models.abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _


class IsinETF(TimeStampedUUIDModel):
    isin = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("ISIN"),
        help_text=_("ISIN")
    )
    ticker = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Ticker"),
        help_text=_("Ticker")
    )
    ticker_yf = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Yahoo Finance Ticker"),
        help_text=_("Yahoo Finance Ticker")
    )
    asset_type = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Asset Type"),
        help_text=_("Asset Type")
    )
    ter = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("TER"),
        help_text=_("TER")
    )

    class Meta:
        verbose_name = _('ETF ISIN')
        verbose_name_plural = _('ETFs ISIN')

    def __str__(self):
        return f"{self.isin} - {self.ticker_yf}"
