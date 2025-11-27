from django.contrib import admin
from .models import AvailableSlot, Appointment


@admin.register(AvailableSlot)
class AvailableSlotAdmin(admin.ModelAdmin):
    list_display = ("start_time", "end_time", "is_booked", "created_at")
    list_filter = ("is_booked",)
    search_fields = ("start_time", "end_time")
    ordering = ("start_time",)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "age", "slot", "status", "created_at")
    search_fields = ("first_name", "last_name", "phone", "slot__start_time")
    list_filter = ("status", "created_at")
    readonly_fields = ("created_at", "updated_at")
