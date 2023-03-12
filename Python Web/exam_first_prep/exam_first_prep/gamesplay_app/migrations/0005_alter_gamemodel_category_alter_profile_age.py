# Generated by Django 4.1.2 on 2022-10-25 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesplay_app', '0004_alter_gamemodel_rating_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='category',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Puzzle', 'Puzzle'), ('Strategy', 'Strategy'), ('Sports', 'Sports'), ('Board/Card Game', 'Board/Card Game'), ('Other', 'Other')], max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(12)]),
        ),
    ]
