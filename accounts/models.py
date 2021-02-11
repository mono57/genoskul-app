from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import related
from django.db.models.signals import post_save

from genoskul.common.timestamp import TimeStampModel
from forum.models import Forum

User = get_user_model()


function_choices = (
    ('eleve', 'Elève'),
    ('student', 'Etudiant'),
    ('unemployed', 'Diplomé sans emploi'),
    ('employed', 'Fonctionnaire'),
    ('entrepreneur', 'Entrepreneur'),
    ('other', 'Autres'),

)


class Speciality(TimeStampModel):
    name = models.CharField(
        max_length=250, verbose_name='Nom de la spécialité')
    description = models.TextField(
        blank=True, verbose_name='Description de la spécialité',
        help_text='Cette description s\affiche comme description du forum associé')

    class Meta:
        verbose_name = 'Spécialité'
        verbose_name_plural = 'Spécialités'

    def __str__(self):
        return self.name

def post_save_speciality_create_forum(sender, instance, created, **kwargs):
    if created:
        Forum.objects.create(
            name=instance.name
        )

post_save.connect(post_save_speciality_create_forum, sender=Speciality)

class Profession(TimeStampModel):
    name = models.CharField(
        max_length=150, verbose_name='Nom de la profession')

    class Meta:
        verbose_name = 'Profession'
        verbose_name_plural = 'Professions'

    def __str__(self):
        return self.name


class SchoolStudentLevel(TimeStampModel):
    level = models.CharField(max_length=50, verbose_name='Nom de la classe')
    description = models.TextField(blank=True, verbose_name='Description')

    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.level


def post_save_school_student_level_create_forum(sender, instance, created, **kwargs):
    if created:
        Forum.objects.create(
            name=instance.level
        )


post_save.connect(post_save_school_student_level_create_forum, sender=SchoolStudentLevel)


class Profile(TimeStampModel):
    avatar = models.ImageField(blank=True, verbose_name='Photo de profile')

    residence = models.CharField(
        max_length=50, blank=True, verbose_name='Pays de résidence')
    nationality = models.CharField(
        max_length=50, blank=True, verbose_name='Nationalité')
    gender = models.CharField(max_length=10, verbose_name='Genre', choices=(
        ('male', 'Masculin'), ('female', 'Feminin')), blank=True)
    birthday = models.DateField(
        verbose_name='Date de naissance', null=True, blank=True)
    telephone = models.CharField(
        max_length=25, verbose_name='Numéro de téléphone', blank=True)
    profession = models.ForeignKey(
        Profession, on_delete=models.DO_NOTHING, verbose_name='Profession', blank=True, null=True)
    speciality = models.ForeignKey(
        Speciality, on_delete=models.DO_NOTHING, verbose_name='Spécialité', blank=True, null=True)

    school_student_level = models.ForeignKey(
        SchoolStudentLevel, on_delete=models.DO_NOTHING, related_name='profiles', blank=True, null=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')


    @property
    def is_student(self):
        return True if self.speciality else False

def post_save_user_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(post_save_user_create_profile, sender=User)
