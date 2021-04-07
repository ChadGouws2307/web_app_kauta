from django.contrib import admin

from .models import Email, UserPermission


class EmailAdmin(admin.ModelAdmin):
    pass


class UserPermissionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Email, EmailAdmin)
admin.site.register(UserPermission, UserPermissionAdmin)
