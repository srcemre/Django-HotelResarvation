from django.contrib import admin

# Register your models here.
from accommodation.models import Category, Hotel, Room, Image


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
    readonly_fields = ('image_tag',)

class HotelAdmin(admin.ModelAdmin):
    list_display = ['category','image_tag','title','star','email','phone','address','city','status']
    readonly_fields = ('image_tag',)
    list_filter  = ['category', 'star', 'city', 'status']
    inlines = [HotelImageInLine]

class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel','image_tag','title','price','amount','person','bed','status']
    list_filter  = ['hotel', 'price', 'person', 'bed','status']
    readonly_fields = ('image_tag',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Image,ImageAdmin)