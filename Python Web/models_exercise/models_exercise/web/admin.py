from django.contrib import admin

from models_exercise.web.models import Employees, Department, Project, ExtraInfo, AccessCard


# Register your models here.

@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'level')
    search_fields = ('first_name', 'last_name', 'level')

    fieldsets = (

                    'Personal Info',
                    {
                        'fields': ('first_name', 'last_name', 'age'),
                    }
                ),


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(ExtraInfo)
class ExtraInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(AccessCard)
class AccessCardAdmin(admin.ModelAdmin):
    pass
