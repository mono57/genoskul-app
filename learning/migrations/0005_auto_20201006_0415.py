# Generated by Django 3.1.1 on 2020-10-06 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_auto_20201006_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='auteur',
            field=models.CharField(blank=True, help_text="NB:Entrez le nom de l'auteur original du document", max_length=150, verbose_name='Auteur du document'),
        ),
    ]