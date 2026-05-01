from django.contrib import admin  # noqa
from apps.users.models import User
from apps.users.resources import UserResources
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.

@admin.register(User)
class UserModelAdmin(ImportExportActionModelAdmin):
    list_display = ['first_name', 'last_name']
    resource_classes = [UserResources]
