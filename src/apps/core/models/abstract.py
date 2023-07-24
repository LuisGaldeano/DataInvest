import uuid
from django.db import models
from model_utils.models import TimeStampedModel


class UUIIDModel(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(UUIIDModel, TimeStampedModel):
    class Meta:
        abstract = True
