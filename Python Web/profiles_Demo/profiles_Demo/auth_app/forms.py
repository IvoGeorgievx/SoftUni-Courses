from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django.db import models

from profiles_Demo.auth_app.models import Profile


class SignUpForm(auth_forms.UserCreationForm):
    age = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = User
        fields = ("username", 'first_name', 'email')
        field_classes = {"username": auth_forms.UsernameField}
        help_texts = {
            'username': None,
            'email': None,
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
            first_name=self.cleaned_data['first_name'],
            email=self.cleaned_data['email'],

        )
        if commit:
            profile.save()
        return user
