from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for the CustomUser model.
    """
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    # Fields to display in the user list
    list_display = ('email', 'first_name', 'last_name', 'date_of_birth', 'is_staff', 'is_active')
    
    # Fields to filter by in the admin
    list_filter = ('is_staff', 'is_active', 'date_joined', 'date_of_birth')
    
    # Fields to search by
    search_fields = ('email', 'first_name', 'last_name')
    
    # Ordering
    ordering = ('email',)
    
    # Fieldsets for the add/edit form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name', 
                'last_name', 
                'date_of_birth', 
                'profile_photo', 
                'bio', 
                'phone_number'
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fieldsets for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 
                'password1', 
                'password2', 
                'first_name', 
                'last_name',
                'date_of_birth',
                'is_staff', 
                'is_active'
            ),
        }),
    )
    
    # Read-only fields
    readonly_fields = ('last_login', 'date_joined')


# Register the custom user model with the admin
admin.site.register(CustomUser, CustomUserAdmin) 