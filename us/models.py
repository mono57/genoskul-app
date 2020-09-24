from django.db import models
from tinymce_4.fields import TinyMCEModelField

from genoskul.common.timestamp import TimeStampModel


SOCIAL_CHOICES = (
    ('facebook', 'Facebook'),
    ('whatsapp', 'Whatsapp'),
    ('telegram', 'Telegram'),
    ('linkedin', 'LinkedIn'),
    ('envelope', 'Gmail'),

)


class SocialNetwork(TimeStampModel):
    name = models.CharField(
        max_length=20,
        verbose_name='Nom du réseau social')
    type = models.CharField(
        max_length=10,
        choices=SOCIAL_CHOICES,
        verbose_name='Type du réseau'
    )
    
    link = models.URLField(verbose_name='Lien direct du réseau social')

    class Meta:
        verbose_name = 'Réseau Social'
        verbose_name_plural = 'Résaux sociaux'


class Footer(TimeStampModel):
    content = models.TextField(verbose_name='Petite de description du pied de page')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Pied de page'
        verbose_name_plural = 'Pieds de page'


class Abstract(TimeStampModel):
    content = TinyMCEModelField('Content')

    class Meta:
        abstract = True


class Privacy(Abstract):
    class Meta:
        verbose_name = 'Politique de confidentialité'
        verbose_name_plural = 'Politiques de confidentialité'


class TermOfService(Abstract):
    class Meta:
        verbose_name = 'Terme de serice'
        verbose_name_plural = 'Termes de serice'


class About(Abstract):
    class Meta:
        verbose_name = 'A propos'
        verbose_name_plural = 'A propos'