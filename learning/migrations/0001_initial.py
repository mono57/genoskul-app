# Generated by Django 3.1.1 on 2020-12-19 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import genoskul.common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Catégorie de document',
                'verbose_name_plural': 'Catégories de document',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Type de document',
                'verbose_name_plural': 'Types de documents',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Nom')),
                ('file', models.FileField(upload_to='', validators=[genoskul.common.validators.file_size], verbose_name='Fichier')),
                ('auteur', models.CharField(help_text="NB:Entrez le nom de l'auteur original du document", max_length=150, verbose_name='Auteur du document')),
                ('download_count', models.IntegerField(blank=True, default=0, verbose_name='Nombre de téléchargements')),
                ('categories', models.ManyToManyField(help_text='Appuyez sur «Ctrl» pour sélectionner plusieurs', related_name='learning', to='learning.DocumentCategory', verbose_name='Catégories')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.documenttype', verbose_name='Type du fichier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL, verbose_name='Créateur')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
    ]
