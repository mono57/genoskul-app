from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from genoskul.common.timestamp import TimeStampModel
# from forum.models import Forum

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

    # function = models.CharField(
    #     max_length=100, blank=True, verbose_name='Fonction', choices=function_choices)
    class Meta:
        abstract = True

class UserProfile(Profile):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Profile utilisateur'
        verbose_name_plural = 'Profiles utilisateurs'

    def __str__(self):
        return self.user.get_username()

class StudentProfile(Profile):
    speciality = models.ForeignKey(Speciality, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='student_profile')

    class Meta:
        verbose_name = 'Profile des étudiants'
        verbose_name_plural = 'Profiles des étudiants'


class SchoolStudentLevel(TimeStampModel):
    level = models.CharField(max_length=30)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='school_student_profile')

    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.level

    
class SchoolStudentProfile(Profile):
    level = models.ForeignKey(SchoolStudentLevel, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Profile des élèves'
        verbose_name_plural = 'Profiles des élèves'


    def __str__(self):
        return self.level.level

    
def post_save_user_create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_save_user_create_profile, sender=User)
