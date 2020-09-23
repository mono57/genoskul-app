from django.db import models
from genoskul.common.timestamp import TimeStampModel


class Box(TimeStampModel):
    type = models.CharField(max_length=150, verbose_name='Type')
    struct_name = models.CharField(
        max_length=150, verbose_name='Nom de la structure')
    struct_description = models.TextField(
        verbose_name='Description de la structure')
    activity_description = models.TextField(
        verbose_name='Description des activités')
    address = models.CharField(
        max_length=100, verbose_name='Adresse de localisation', help_text='Quartier/Ville/Pays')

    contact = models.CharField(max_length=50, verbose_name='Contact')

    logo = models.ImageField(verbose_name='Logo de la boite')


    def __str__(self):
        return self.struct_name