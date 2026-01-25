from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Display these fields in the admin list view
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    
    # Add custom fields to the user editing page
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # Add custom fields to the 'Add User' page
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register your CustomUser with the CustomAdmin
admin.site.register(CustomUser, CustomUserAdmin)