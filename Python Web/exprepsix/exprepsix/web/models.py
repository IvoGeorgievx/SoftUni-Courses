from django.core import validators
from django.db import models


class Profile(models.Model):
    MAX_LENGTH_NAME = 30
    email = models.EmailField(null=False, blank=False)

    age = models.PositiveIntegerField(null=False,
                                      blank=False,
                                      validators=[validators.MinValueValidator(12.0)],
                                      )

    password = models.CharField(null=False, blank=False, max_length=30)

    first_name = models.CharField(null=True, blank=True, max_length=MAX_LENGTH_NAME)

    last_name = models.CharField(null=True, blank=True, max_length=MAX_LENGTH_NAME)

    profile_picture = models.URLField(null=True, blank=True)


class GameModel(models.Model):
    possible_choices = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    title = models.CharField(null=False,
                             blank=False,
                             unique=True,
                             max_length=30,
                             )

    category = models.CharField(null=False,
                                blank=False,
                                max_length=15,
                                choices=possible_choices,
                                )

    rating = models.FloatField(null=False,
                               blank=False,
                               validators=[validators.MinValueValidator(0.1),
                                           validators.MaxValueValidator(5.0)],
                               )

    max_level = models.PositiveIntegerField(null=True,
                                            blank=True,
                                            validators=[validators.MinValueValidator(1.0)],
                                            )

    image_url = models.URLField(null=False, blank=False)

    summary = models.TextField(null=True, blank=True)
