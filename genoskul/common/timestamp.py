from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Date de création', auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        verbose_name='Date de modification', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True