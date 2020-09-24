# Generated by Django 3.1.1 on 2020-09-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('name', models.CharField(max_length=20, verbose_name='Nom du réseau social')),
                ('type', models.CharField(choices=[('facebook', 'Facebook'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('linkedin', 'LinkedIn'), ('envelope', 'Gmail')], max_length=10, verbose_name='Type du réseau')),
                ('link', models.URLField(verbose_name='Lien direct du réseau social')),
            ],
            options={
                'verbose_name': 'Réseau Social',
                'verbose_name_plural': 'Résaux sociaux',
            },
        ),
    ]
