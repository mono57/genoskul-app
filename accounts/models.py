from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from genoskul.common.timestamp import TimeStampModel


User = get_user_model()


function_choices = (
    ('eleve', 'Elève'),
    ('student', 'Etudiant'),
    ('unemployed', 'Diplomé sans emploi'),
    ('employed', 'Fonctionnaire'),
    ('entrepreneur', 'Entrepreneur'),
    ('other', 'Autres'),

)

class Profile(TimeStampModel):
    avatar = models.ImageField(blank=True, verbose_name='Photo de profile')

    residence = models.CharField(
        max_length=50, blank=True, verbose_name='Lieu de résidence')
    nationality = models.CharField(
        max_length=50, blank=True, verbose_name='Nationalité')
    gender = models.CharField(max_length=10, verbose_name='Genre', choices=(
        ('male', 'Masculin'), ('female', 'Feminin')), blank=True)
    birthday = models.DateField(
        blank=True, null=True, verbose_name='Date de naissance')
    telephone = models.CharField(
        max_length=25, verbose_name='Numéro de téléphone', blank=True)

    function = models.CharField(max_length=100, blank=True, verbose_name='Fonction', choices=function_choices)

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')


def post_save_user_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(post_save_user_create_profile, sender=User)
