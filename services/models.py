from django.db import models
from django.contrib.auth import get_user_model
from genoskul.common.timestamp import TimeStampModel
from genoskul.common.validators import file_size

User = get_user_model()


class ServiceManager(models.Manager):
    def get_confirmed_services(self):
        qs = self.get_queryset()
        return qs.filter(confirmed=True)


class BoxType(TimeStampModel):
    name = models.CharField(max_length=150, verbose_name='Nom du type')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type de service'
        verbose_name_plural = 'Types de services'

class Box(TimeStampModel):
    type = models.ForeignKey(BoxType, verbose_name='Type de service',
                             on_delete=models.CASCADE, related_name='services')
    struct_name = models.CharField(
        max_length=150, verbose_name='Nom de la structure', help_text="Nom &  prenoms si c'est une personne")
    struct_description = models.TextField(
        verbose_name='Description de la structure', help_text="Biographie si c'est une personne")
    activity_description = models.TextField(
        verbose_name='Description des activités', help_text="Qu'est ce que vous et/ou votre structure faites?")
    address = models.CharField(
        max_length=100, verbose_name='Adresse de localisation', help_text='Quartier/Ville/Pays')

    contact = models.CharField(max_length=50, verbose_name='Contact', help_text="adress mail ou numero whatsapp" )

    logo = models.ImageField(verbose_name='Logo de la boite', validators=[file_size])

    detail_link = models.URLField(verbose_name='Lien', help_text="lien du site de votre structure ou de votre page")

    confirmed = models.BooleanField(default=False, verbose_name='Confirmé ?')

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='services')

    objects = ServiceManager()

    def __str__(self):
        return self.struct_name
