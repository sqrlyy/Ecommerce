from django.contrib import admin

from home.models import Setting


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'status']
    list_filter = ['company']


admin.site.register(Setting, SettingsAdmin)

