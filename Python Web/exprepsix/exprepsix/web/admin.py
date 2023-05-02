from django.contrib import admin

from exprepsix.web.models import Profile, GameModel


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    pass
