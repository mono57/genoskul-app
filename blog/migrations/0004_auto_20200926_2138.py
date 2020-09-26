# Generated by Django 3.1.1 on 2020-09-26 20:38

from django.db import migrations, models
import genoskul.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/', validators=[genoskul.common.validators.file_size], verbose_name='Image de couverture'),
        ),
    ]
