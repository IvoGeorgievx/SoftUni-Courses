from django import forms

from epfour.web.models import Profile, Note


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(BaseProfileForm):
    pass


class ProfileDeleteForm(BaseProfileForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Note.objects.all().delete()
        return self.instance


class BaseNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class NoteCreateForm(BaseNoteForm):
    pass


class EditNoteForm(BaseNoteForm):
    pass


class DeleteNoteForm(BaseNoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
