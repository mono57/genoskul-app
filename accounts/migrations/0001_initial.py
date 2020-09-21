# Generated by Django 3.1.1 on 2020-09-21 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('avatar', models.ImageField(blank=True, upload_to='', verbose_name='Photo de profile')),
                ('residence', models.CharField(blank=True, max_length=50, verbose_name='Lieu de résidence')),
                ('nationality', models.CharField(blank=True, max_length=50, verbose_name='Nationalité')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Masculin'), ('female', 'Feminin')], max_length=10, verbose_name='Genre')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Date de naissance')),
                ('telephone', models.CharField(blank=True, max_length=25, verbose_name='Numéro de téléphone')),
                ('function', models.CharField(blank=True, choices=[('eleve', 'Elève'), ('student', 'Etudiant'), ('unemployed', 'Diplomé sans emploi'), ('employed', 'Fonctionnaire'), ('entrepreneur', 'Entrepreneur'), ('other', 'Autres')], max_length=100, verbose_name='Fonction')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
