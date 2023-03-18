from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_length(value):
    if len(value) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


#
def validate_year(value):
    if value > 2049:
        raise ValidationError("Year must be between 1980 and 2049")
    if value < 1980:
        raise ValidationError("Year must be between 1980 and 2049")


class Profile(models.Model):
    MAX_LENGTH_PASSWORD = 30
    MAX_LENGTH_NAME = 30
    MAX_LENGTH_USERNAME = 10

    username = models.CharField(null=False,
                                blank=False,
                                validators=[validate_length],
                                max_length=MAX_LENGTH_USERNAME,
                                )

    email = models.EmailField(null=False,
                              blank=False,
                              )

    age = models.PositiveIntegerField(null=False,
                                      blank=False,
                                      validators=[validators.MinValueValidator(18)]

                                      )

    password = models.CharField(null=False,
                                blank=False,
                                max_length=MAX_LENGTH_PASSWORD,
                                )

    first_name = models.CharField(null=True,
                                  blank=True,
                                  max_length=MAX_LENGTH_NAME,
                                  )

    last_name = models.CharField(null=True,
                                 blank=True,
                                 max_length=MAX_LENGTH_NAME,
                                 )

    profile_picture = models.URLField(null=True,
                                      blank=True,
                                      )


class Car(models.Model):
    TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 20
    possible_choices = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )

    type = models.CharField(null=False,
                            blank=False,
                            choices=possible_choices,
                            max_length=TYPE_MAX_LENGTH,
                            )

    model = models.CharField(null=False,
                             blank=False,
                             max_length=MODEL_MAX_LENGTH,
                             validators=[validators.MinLengthValidator(2)],
                             )

    year = models.PositiveIntegerField(null=False,
                                       blank=False,
                                       validators=[validate_year],
                                       )

    image_url = models.URLField(null=False,
                                blank=False,
                                )

    price = models.FloatField(null=False,
                              blank=False,
                              validators=[validators.MinValueValidator(1.0)]
                              )
