from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#models
from django.contrib.auth.models import User
from clientes.models import ProfileCliente
# Register your models here.

@admin.register(ProfileCliente)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display= ('user','country','city', 'category')
    list_display_links = ('user','country')
    # list_editable = ('city')
    search_fields=(
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',        
        )
    list_filter = ('country', 'city', 'category')

    fieldsets = (
        (None, {
            'fields': ('user', 'category')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('country','city'),
        }),
    )

    readonly_fields=('user_created','user_modifed',)

class ProfileInline(admin.StackedInline):
    model = ProfileCliente
    can_delete = False
    verbose_name_plural = 'profileclientes'

class UserAdmin(BaseUserAdmin):
    inlines=(ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)