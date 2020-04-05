from django.contrib import admin

# Register your models here.
from home.models import Settings, ContactFormMessage


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'address', 'phone', 'fax', 'email', 'icon', 'facebook', 'instagram', 'twitter', 'status']


class ContactForMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']


admin.site.register(Settings, SettingsAdmin)
admin.site.register(ContactFormMessage, ContactForMessageAdmin)
