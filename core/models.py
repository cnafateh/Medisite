from django.db import models
from django.conf import settings


class SiteSettings(models.Model):
    clinic_name = models.CharField(max_length=255)
    clinic_address = models.CharField(max_length=255)
    clinic_phone = models.CharField(max_length=50)
    hospital_name = models.CharField(max_length=150)
    hospital_address = models.CharField(max_length=255)
    hospital_phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    instagram = models.CharField(max_length=150)
    telegram = models.CharField(max_length=150)
    whatsapp = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    footer_text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"

    def __str__(self):
        return "Site Settings"


def doctor_profile_upload_path(instance, filename):
    return f"doctor/profile/{filename}"


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True,  
        blank=True  
    )
    full_name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    biography = models.TextField()
    medical_registry_number = models.CharField(max_length=100)
    experience_years = models.PositiveSmallIntegerField()
    profile_image = models.ImageField(upload_to=doctor_profile_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
