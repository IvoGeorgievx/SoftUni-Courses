from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=25)

    last_name = models.CharField(max_length=25)

    age = models.PositiveIntegerField(blank=True,
                                      null=True, )

    email = models.EmailField(null=False, blank=False)

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
