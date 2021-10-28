from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('firstname', 'lastname', 'patronymic')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            # show additional fields when I wanna add a new user on the admin panel
            'fields': ('firstname', 'lastname', 'patronymic', 'email', 'password'),
        }),
    )
    # display fields of users on the admin panel 
    list_display = ('email', 'firstname', 'lastname', 'patronymic', 'is_staff')
    search_fields = ('email', 'firstname', 'lastname')
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)
