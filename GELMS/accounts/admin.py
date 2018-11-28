from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from accounts.models import CustomUser
from django.utils.translation import ugettext_lazy as _


class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'Details'
    exclude = ['reader_mode','multifactor',]


class CustomUserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', ),
        }),
    )

    inlines = (CustomUserInline,)

    fieldsets = (
        (_('Account'), {'fields': ('username','email','password',)}),
        (_('Name'), {'fields': ('first_name', 'last_name',)}),
        )

    list_display = ('email', 'get_uid', 'get_status',)
    list_filter = ('custom_user__status',)
    ordering = ()

    def get_uid(self, instance):
        return instance.custom_user.uid
    get_uid.short_description = 'UID'

    def get_status(self, instance):
        return instance.custom_user.status
    get_status.short_description = 'Status'

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        return qs.filter(is_superuser=False)




# Registrations:
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
