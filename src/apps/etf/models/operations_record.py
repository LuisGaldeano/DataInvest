from django.db import models
from ...core.models.abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from .etf_isin import IsinETF


class OperationsRecord(TimeStampedUUIDModel):
    date = models.DateField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Date"),
        help_text=_("Date")
    )
    price = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Price"),
        help_text=_("Price")
    )
    buy_or_sale = models.IntegerField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Buy or sale"),
        help_text=_("1 if it is Buy, 2 if it is sale")
    )

    shares_number = models.IntegerField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Number of stock shares"),
        help_text=_("Number of stock shares")
    )
    commissions = models.IntegerField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Commissions"),
        help_text=_("Commissions")
    )
    capital_contribution = models.FloatField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Capital Contribution"),
        help_text=_("Capital Contribution")
    )

    isin = models.ForeignKey(IsinETF, on_delete=models.CASCADE, to_field='uuid')

    class Meta:
        verbose_name = _('Operation Record')
        verbose_name_plural = _('Operations Record')

    def __str__(self):
        return f"{self.date} - {self.isin}: {self.capital_contribution})"
