# Generated by Django 4.0.2 on 2022-02-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platformUsers', '0002_alter_platformuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformuser',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
    ]