from django import forms

from exprepsix.web.models import Profile, GameModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
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
            GameModel.objects.all().delete()
        return self.instance


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class CreateGameForm(BaseGameForm):
    pass


class EditGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
