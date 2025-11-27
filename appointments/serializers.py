from rest_framework import serializers
from .models import AvailableSlot, Appointment
from django.utils import timezone


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableSlot
        fields = ("id", "start_time", "end_time", "is_booked")


class AppointmentCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20, allow_blank=True, required=False)
    age = serializers.IntegerField(min_value=0, required=False)
    preferred_date = serializers.DateField(required=True)
    preferred_time = serializers.TimeField(required=True)
    description = serializers.CharField(allow_blank=True, required=False)

    def validate(self, data):
        # تبدیل preferred_date + preferred_time به یک datetime aware
        dt = timezone.make_aware(
            timezone.datetime.combine(data["preferred_date"], data["preferred_time"]),
            timezone.get_current_timezone()
        )
        data["preferred_datetime"] = dt
        # disallow past dates
        if dt < timezone.now():
            raise serializers.ValidationError("زمان انتخابی گذشته است.")
        return data


class AppointmentSerializer(serializers.ModelSerializer):
    slot = SlotSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = (
            "id",
            "first_name", "last_name", "phone", "age",
            "preferred_datetime",
            "slot",
            "description",
            "status",
            "created_at",
        )
