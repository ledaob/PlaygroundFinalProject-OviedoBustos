from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import User_profile

@admin.register
class User_profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_staff')
    list_filter= ('nombre')
    search_fields = ('nombre', 'correo')


class UserProfileInline(admin.StackedInline):
    model = User_profile
    can_delete = False
    verbose_name_plural = 'User Profiles'

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]
    filter_horizontal= ('groups')
    ordering = ('nombre')
    list_display = ('nombre')



admin.site.register(User_profile, UserAdmin)
admin.site.unregister(User_profile)





