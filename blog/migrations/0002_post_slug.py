# Generated by Django 4.0.1 on 2022-01-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='introduction-to-python', max_length=255),
            preserve_default=False,
        ),
    ]
