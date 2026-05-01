from django.contrib import admin  # noqa
from apps.users.models import User
# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']