from rest_framework import serializers
from .models import AvailableSlot, Appointment
from django.utils import timezone


class AvailableSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableSlot
        fields = "__all__"
        read_only_fields = ["doctor", "is_booked"]

    def validate(self, data):
        start = data["start_time"]
        end = data["end_time"]

        if start >= end:
            raise serializers.ValidationError("زمان شروع باید قبل از پایان باشد.")

        # چک همپوشانی تایم‌ها
        doctor = self.context["request"].user
        qs = AvailableSlot.objects.filter(doctor=doctor)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        overlap = qs.filter(
            start_time__lt=end,
            end_time__gt=start
        ).exists()

        if overlap:
            raise serializers.ValidationError("این بازه زمانی با تایم دیگر همپوشانی دارد.")

        return data


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ["patient", "status"]

    def validate_slot(self, slot):
        if slot.is_booked:
            raise serializers.ValidationError("این تایم قبلاً رزرو شده است.")
        return slot
