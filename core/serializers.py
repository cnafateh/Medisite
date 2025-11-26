from rest_framework import serializers
from .models import DoctorProfile, SiteSettings


# ---------------------------
# Doctor Profile Serializer
# ---------------------------
class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = "__all__"


# ---------------------------
# Site Settings Serializer
# ---------------------------
class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"


# ---------------------------
# Footer Serializer (Combined)
# ---------------------------
class FooterSerializer(serializers.ModelSerializer):
    # این دوتا فیلد از DoctorProfile وارد می‌شن
    full_name = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)

    class Meta:
        model = SiteSettings
        fields = [
            "full_name",
            "title",
            "footer_text",
            "clinic_name",
            "clinic_address",
            "clinic_phone",
            "hospital_name",
            "hospital_address",
            "hospital_phone",
            "email",
            "instagram",
            "telegram",
            "whatsapp",
            "website",
            "location_lat",
            "location_lng",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        doctor = DoctorProfile.objects.first()

        data["full_name"] = doctor.full_name if doctor else ""
        data["title"] = doctor.title if doctor else ""

        return data