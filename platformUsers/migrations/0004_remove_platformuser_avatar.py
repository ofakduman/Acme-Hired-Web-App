# Generated by Django 4.0.2 on 2022-02-22 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platformUsers', '0003_platformuser_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platformuser',
            name='avatar',
        ),
    ]
