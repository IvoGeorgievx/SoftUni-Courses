from django.contrib import admin

from first_django_project.tasks.models import Task


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority')
