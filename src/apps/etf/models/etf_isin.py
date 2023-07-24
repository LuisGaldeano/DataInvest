from django.db import models
from ...core.models.abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from .etf_asset_type import AssetType
from .etf_underlying import Underlying


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
    ter = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("TER"),
        help_text=_("TER")
    )

    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE, to_field='uuid')
    underlying = models.ForeignKey(Underlying, on_delete=models.CASCADE, to_field='uuid')

    class Meta:
        verbose_name = _('ETF ISIN')
        verbose_name_plural = _('ETFs ISIN')

    def __str__(self):
        return f"{self.isin} - {self.ticker_yf}"
