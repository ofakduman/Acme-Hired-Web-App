# Generated by Django 4.0.2 on 2022-02-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platformUsers', '0014_platformuser_bio_platformuser_blog_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platformuser',
            name='bio',
            field=models.TextField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='platformuser',
            name='blog',
            field=models.TextField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='platformuser',
            name='company',
            field=models.TextField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='platformuser',
            name='email',
            field=models.TextField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='platformuser',
            name='html_url',
            field=models.TextField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='platformuser',
            name='location',
            field=models.TextField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='platformuser',
            name='login',
            field=models.TextField(default='null', max_length=200),
        ),
    ]