from django.contrib import admin

# Register your models here.
from reservation.models import ReservationRoom, Reservation


class ReservationRoomline(admin.TabularInline):
    model = ReservationRoom
    readonly_fields = ('user', 'room', 'price', 'quantity', 'amount','person','checkin','checkout')
    can_delete = False
    extra = 0


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'total', 'status']
    list_filter = ['status']
    readonly_fields = (
        'user', 'first_name', 'last_name', 'address', 'city', 'country', 'phone', 'ip', 'total')
    can_delete = False
    inlines = [ReservationRoomline]


class ReservationRoomAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'price', 'quantity', 'amount','person','checkin','checkout']
    list_filter = ['user']


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationRoom, ReservationRoomAdmin)
