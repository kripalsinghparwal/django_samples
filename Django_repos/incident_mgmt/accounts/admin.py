from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Extra Info', {
            'fields': ('phone', 'address', 'pincode', 'city', 'country')
        }),
    )
    list_display = ('username', 'email', 'phone', 'pincode', 'city', 'country')
    search_fields = ('username', 'email', 'phone', 'pincode', 'city', 'country')

admin.site.register(User, UserAdmin)
