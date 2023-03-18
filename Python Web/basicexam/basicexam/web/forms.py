from django import forms

from basicexam.web.models import Profile, Car


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password',)
        widgets = {
            'password': forms.PasswordInput
        }


class EditProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # widgets = {
        #     'password': forms.PasswordInput
        # }
        # TODO FIX hidden/shown password


class DeleteProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Car.objects.all().delete()
        return self.instance


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            # TODO DISABLE DROPDOWN

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
