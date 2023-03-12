from django.contrib import admin

from exam_first_prep.gamesplay_app.models import Profile, GameModel


# Register your models here.
@admin.register(Profile)
class ProfileReg(admin.ModelAdmin):
    pass


@admin.register(GameModel)
class GameModelReg(admin.ModelAdmin):
    pass
