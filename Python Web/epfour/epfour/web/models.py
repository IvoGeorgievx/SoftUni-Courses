from django.db import models


# Create your models here.


class Profile(models.Model):
    MAX_LENGTH_NAME = 20

    first_name = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_NAME)

    last_name = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_NAME)

    age = models.IntegerField(null=False, blank=False)

    image_URL = models.URLField(null=False, blank=False)


class Note(models.Model):
    MAX_LENGTH_TITLE = 30

    title = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_TITLE)

    image_URL = models.URLField(null=False, blank=False)

    content = models.TextField(null=False, blank=False)
