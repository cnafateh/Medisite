# core/admin.py
from django.contrib import admin
from .models import DoctorProfile, SiteSettings

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'user')
    exclude = ('user',)  # user خودکار ست شود


    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        obj.save()


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('clinic_name', 'hospital_name')
