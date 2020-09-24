from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from genoskul.common.timestamp import TimeStampModel

from jobs.managers import JobManager, ResumeManager

User = get_user_model()


class AbstractJob(TimeStampModel):
    name = models.CharField(max_length=50, verbose_name='Nom')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class JobType(AbstractJob):
    class Meta:
        verbose_name = 'Type d\'emploi'
        verbose_name_plural = 'Types d\'emplois'


class JobCategory(AbstractJob):
    linear_icon = models.CharField(max_length=50, verbose_name='Icon')
    
    class Meta:
        verbose_name = 'Secteur d\'emploi'
        verbose_name_plural = 'Secteurs d\'emplois'


    def get_absolute_url(self):
        return reverse('jobs:category-detail', kwargs={'pk': self.pk})


class Company(TimeStampModel):
    name = models.CharField(max_length=100, verbose_name='Nom')
    website = models.URLField(blank=True, verbose_name='URL site internet')
    tagline = models.CharField(
        max_length=255, verbose_name='Brève description', blank=True)
    logo = models.ImageField(verbose_name='Logo', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Entreprise'
        verbose_name_plural = 'Entreprises'


class Job(TimeStampModel):
    title = models.CharField(max_length=200, verbose_name='Titre')
    type = models.ForeignKey(
        JobType, verbose_name='Type', on_delete=models.CASCADE)
    category = models.ManyToManyField(JobCategory, related_name='jobs', verbose_name='Secteur d\'emploi')
    location = models.CharField(
        max_length=100, verbose_name='Lieu d\'execution', blank=True)
    # tags = models.CharField(max_length=255, verbose_name='Tags', blank=True)
    description = models.TextField(verbose_name='Description du poste')
    application_email = models.EmailField(
        verbose_name='Adresse email de postulat')
    closing_date = models.DateField(
        verbose_name='Date de fermeture', blank=True, null=True)
    company = models.ForeignKey(
        Company, verbose_name='Entreprise', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, verbose_name='Créateur', related_name='jobs', on_delete=models.CASCADE)

    objects = JobManager()

    def get_absolute_url(self):
        return reverse("jobs:job-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Offre d\'emploi'
        verbose_name_plural = 'Offres d\'emplois'


class Resume(TimeStampModel):
    pro_title = models.CharField(
        max_length=200, verbose_name='Titre professionel')
    location = models.CharField(
        max_length=150, verbose_name='Lieu de résidence')
    website = models.URLField(verbose_name='Lien du portfolio', blank=True)
    resume_file = models.FileField(
        verbose_name='Fichier CV', upload_to='resumes')

    contact = models.CharField(
        max_length=255, verbose_name='Votre contact', help_text='Aidez les récruteurs à vous contacter')

    description = models.TextField(verbose_name='A propos de vous')

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='resumes')

    objects = ResumeManager()

    def get_absolute_url(self):
        return reverse("jobs:resume-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return '{} : {}'.format(self.pro_title, self.user.first_name)
