from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1',
                       'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'username', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['first_name', 'last_name', 'email', 'username', ]
    search_fields = ('email', 'username')
    ordering = ('email',)
    list_display_links = ['first_name', 'last_name', 'email', 'username', ]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
