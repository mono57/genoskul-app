# Generated by Django 3.1.1 on 2020-09-18 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200913_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='telephone',
            field=models.CharField(blank=True, max_length=25, verbose_name='Numéro de téléphone'),
        ),
    ]
