from django.contrib import admin

from epfive.web.models import Recipe


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass