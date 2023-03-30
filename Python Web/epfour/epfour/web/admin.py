from django.contrib import admin

from epfour.web.models import Profile, Note


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass