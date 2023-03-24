from django import forms

from examprep3.web.models import Book, Profile


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AddBookForm(BaseBookForm):
    pass


class EditBookForm(BaseBookForm):
    pass


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Book.objects.all().delete()
        return self.instance

    def __disable_fields(self):
        for _, fields in self.fields.items():
            fields.widget.attrs['readonly'] = 'readonly'
