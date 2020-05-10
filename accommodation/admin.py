from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from accommodation.models import Category, Accommodation, Room, Image, Comment


class HotelImageInLine(admin.TabularInline):
    model = Image
    extra = 5

class ImageAdmin(admin.ModelAdmin):
    list_display = ['hotel','title','image_tag','image']
    list_filter  = ['hotel']
    readonly_fields = ('image_tag',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status','parent','image_tag']
    list_filter  = ['status','parent']

class HotelAdmin(admin.ModelAdmin):
    list_display = ['category','image_tag','title','star','email','phone','address','city','status']
    readonly_fields = ('image_tag',)
    list_filter  = ['category', 'star', 'city', 'status']
    inlines = [HotelImageInLine]
    prepopulated_fields = {'slug':('title',)}

class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel','image_tag','title','price','amount','person','bed','status']
    list_filter  = ['hotel', 'price', 'person', 'bed','status']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin2(DraggableMPTTAdmin):

    mptt_indent_field = "title"
    list_display = ('tree_actions',  'indented_title', 'image_tag',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Accommodation,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Accommodation,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'hotel', 'user', 'status']
    list_filter = ['status']

admin.site.register(Category,CategoryAdmin2)
admin.site.register(Accommodation,HotelAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Comment,CommentAdmin)