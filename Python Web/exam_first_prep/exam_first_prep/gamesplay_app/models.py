from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django import forms


class Profile(models.Model):
    email = models.EmailField(blank=False, null=False)

    age = models.PositiveIntegerField(blank=False, null=False,
                                      validators=[MinValueValidator(12)],
                                      )

    password = models.CharField(blank=False, null=False, max_length=30)

    first_name = models.CharField(max_length=30, blank=True)

    last_name = models.CharField(max_length=30, blank=True)

    profile_picture = models.URLField(blank=True)

    def __str__(self):
        return f'{self.email}: {self.age}'


class GameModel(models.Model):
    possible_choices = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other")
    )

    title = models.CharField(null=False, blank=False,
                             max_length=30)

    category = models.CharField(max_length=15,
                                choices=possible_choices,
                                null=False,
                                blank=False, )

    rating = models.FloatField(null=False,
                               blank=False,
                               validators=[MinValueValidator(0.1), MaxValueValidator(5)],
                               default=0
                               )

    max_level = models.IntegerField(blank=True,
                                    validators=[MinValueValidator(1)],
                                    default=0)

    image_URL = models.URLField()

    summary = models.TextField(blank=True)

    def __str__(self):
        return f'Category: {self.category}, Title: {self.title}, Rating:{self.rating}'


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput
        }


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __disabled_field(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class GameBaseForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class CreateGameForm(GameBaseForm):
    pass


class EditGameForm(GameBaseForm):
    pass


class DeleteGameForm(GameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disabled_field()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __disabled_field(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
