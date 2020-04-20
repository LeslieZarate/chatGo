from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # cifrado la contrseña
from .models import User

class CustomUserAdmin(UserAdmin):
    ordering = ('id',)
    list_display = ('id','email', 'username','is_staff','is_active')
    #search_fields = ('email', 'username',)

    readonly_fields = ('date_joined', 'last_login')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birth_date','avatar')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
       (None, {'fields': ('email','is_staff','is_active','birth_date')}),
    )

admin.site.register(User, CustomUserAdmin)

# https://static.turbosquid.com/Preview/001292/481/WV/_D.jpg