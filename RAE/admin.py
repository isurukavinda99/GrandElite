from django.contrib import admin
from .models import Room, RoomBooking, EventBooking

# Register your models here.
admin.site.register(Room)
class RoomDataAdmin(admin.ModelAdmin):
    list_display = ['room_id', 'type', 'price', 'description', 'status']

admin.site.register(RoomBooking)
class RoomBookingDataAdmin(admin.ModelAdmin):
    list_display = ['reserve_id', 'room_Id', 'customer_name', 'customer_phone', 'customer_email', 'check_in', 'check_out']


admin.site.register(EventBooking)
class EventBookingDataAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'event_type', 'package', 'price', 'customer_name', 'customer_phone', 'customer_email', 'date', 'time_in', 'time_out']

