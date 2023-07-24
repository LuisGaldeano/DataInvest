from django.db import models
from ...core.models.abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from .etf_isin import IsinETF


class InfoETF(TimeStampedUUIDModel):
    currency = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Currency"),
        help_text=_("Currency")
    )

    fundFamily = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Fund Family"),
        help_text=_("Fund Family")
    )
    fundInceptionDate = models.IntegerField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Fund Inception Date"),
        help_text=_("Fund Inception Date")
    )
    legalType = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Legal Type"),
        help_text=_("Legal Type")
    )

    exchange = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Exchange"),
        help_text=_("Exchange")
    )
    quoteType = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Quote Type"),
        help_text=_("Quote Type")
    )
    symbol = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Symbol"),
        help_text=_("Symbol")
    )
    underlyingSymbol = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Underlying Symbol"),
        help_text=_("Underlying Symbol")
    )
    shortName = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Short Name"),
        help_text=_("Short Name")
    )
    longName = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Long Name"),
        help_text=_("Long Name")
    )
    firstTradeDateEpochUTC = models.IntegerField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("First Trade Date Epoch Utc"),
        help_text=_("Regular Market Open")
    )
    timeZoneFullName = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Time Zone Full Name"),
        help_text=_("Time Zone Full Name")
    )
    timeZoneShortName = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Time Zone Short Name"),
        help_text=_("Time Zone Short Name")
    )
    external_uuid = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("External uuid"),
        help_text=_("External uuid")
    )
    messageBoardId = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Message Board Id"),
        help_text=_("Message Board Id")
    )

    isin = models.ForeignKey(IsinETF, on_delete=models.CASCADE, to_field='uuid')

    class Meta:
        verbose_name = _('ETF Info')
        verbose_name_plural = _('ETFs Info')

    def __str__(self):
        return f"{self.isin} - {self.shortName}"
