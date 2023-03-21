from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
def validate_string(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=(validators.MinLengthValidator(2),
                    validate_string
                    ))
    email = models.EmailField(null=False,
                              blank=False,)

    age = models.PositiveIntegerField(null=True,
                                      blank=True,)


class Album(models.Model):
    possible_choices = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    )
    album_name = models.CharField(null=False,
                                  blank=False,
                                  unique=True,
                                  max_length=30)

    artist = models.CharField(max_length=30,
                              blank=False,
                              null=False,)

    genre = models.CharField(blank=False,
                             null=False,
                             choices=possible_choices,
                             max_length=30,)

    description = models.TextField(null=True,
                                   blank=True,)

    image_url = models.URLField(blank=False,
                                null=False,)

    price = models.FloatField(null=False,
                              blank=False,
                              # validators=(MinValueValidator(0.0)),

                              )

