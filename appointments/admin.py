# appointments/admin.py
from django.contrib import admin
from .models import AvailableSlot, Appointment

@admin.register(AvailableSlot)
class AvailableSlotAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'start_time', 'end_time', 'is_booked')
    exclude = ('doctor',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Doctor').exists():
            return qs.filter(doctor=request.user)
        return qs

    def has_change_permission(self, request, obj=None):
        if obj and request.user.groups.filter(name='Doctor').exists():
            return obj.doctor == request.user
        return super().has_change_permission(request, obj)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.doctor = request.user
        obj.save()


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'slot', 'status')
    exclude = ('patient',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Patient').exists():
            return qs.filter(patient=request.user)
        if request.user.groups.filter(name='Doctor').exists():
            # دکتر همه نوبت‌ها را می‌بیند
            return qs
        return qs

    def save_model(self, request, obj, form, change):
        if not obj.pk and request.user.groups.filter(name='Patient').exists():
            obj.patient = request.user
        obj.save()
