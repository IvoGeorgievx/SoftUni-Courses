from django.core.validators import MinValueValidator, EmailValidator
from django.db import models


# Create your models here.


class Profile(models.Model):
    MAX_NAME_LENGTH = 30
    first_name = models.CharField(max_length=MAX_NAME_LENGTH, null=False, blank=False)

    last_name = models.CharField(max_length=MAX_NAME_LENGTH, null=False, blank=False)

    image_URL = models.URLField(null=False, blank=False)


class Book(models.Model):
    MAX_LENGTH_CHARS = 30

    title = models.CharField(max_length=MAX_LENGTH_CHARS, null=False, blank=False)

    description = models.TextField(null=False, blank=False)

    image = models.URLField(null=False, blank=False)

    type = models.CharField(max_length=MAX_LENGTH_CHARS, null=False, blank=False, validators=[EmailValidator])

