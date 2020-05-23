from django.contrib import admin
# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from content.models import CImages, Content, Menu


class ContentImageInLine(admin.TabularInline):
    model = CImages
    extra = 3


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title','user','type','image_tag', 'status', 'create_at']
    list_filter = ['type', 'status','user']
    inlines = [ContentImageInLine]
    prepopulated_fields = {'slug': ('title',)}


class MenuAdmin(DraggableMPTTAdmin):
    mptt_level_indent = "title"
    list_display = ['tree_actions', 'indented_title','status']
    list_filter = ['status']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Content, ContentAdmin)
