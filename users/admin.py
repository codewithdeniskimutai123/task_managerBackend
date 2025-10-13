from django.contrib import admin
from .models import CustomeUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomeUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'bio', 'profile_picture')

    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'bio', 'profile_picture')}),
    )




admin.site.register(CustomeUser, CustomeUserAdmin)