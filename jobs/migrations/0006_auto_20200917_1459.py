# Generated by Django 3.1.1 on 2020-09-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200917_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='closing_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date de fermeture'),
        ),
    ]
