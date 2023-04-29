from django.db import models


# Create your models here.
class Recipe(models.Model):

    title = models.CharField(max_length=30, null=False, blank=False)

    image_URL = models.URLField(null=False, blank=False)

    description = models.TextField(null=False, blank=False)

    ingredients = models.CharField(max_length=250, null=False, blank=False)

    time = models.IntegerField(null=False, blank=False)
