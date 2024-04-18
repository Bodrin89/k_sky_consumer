from django.contrib import admin

from apps.user.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role')
    list_display_links = ('id', 'username')
