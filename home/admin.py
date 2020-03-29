from django.contrib import admin

# Register your models here.
from home.models import Settings


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title','company','address','phone','fax','email','icon','facebook','instagram','twitter','status']

admin.site.register(Settings,SettingsAdmin)