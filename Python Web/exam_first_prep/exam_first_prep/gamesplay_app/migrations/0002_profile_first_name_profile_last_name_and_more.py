# Generated by Django 4.1.2 on 2022-10-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesplay_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(blank=True),
        ),
    ]
