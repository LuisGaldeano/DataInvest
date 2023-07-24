from django.db import models
from ...core.models.abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _


class AssetType(TimeStampedUUIDModel):
    asset_type = models.CharField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Asset Type"),
        help_text=_("Asset Type")
    )

    class Meta:
        verbose_name = _('Asset Type')
        verbose_name_plural = _('Assets Type')

    def __str__(self):
        return f"{self.asset_type}"