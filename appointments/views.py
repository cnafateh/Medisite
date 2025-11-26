from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import AvailableSlot, Appointment
from .serializers import AvailableSlotSerializer, AppointmentSerializer


# ------------------------
# پزشک: ایجاد تایم خالی
# ------------------------
class AvailableSlotListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AvailableSlotSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or hasattr(user, "doctor_profile"):
            return AvailableSlot.objects.filter(doctor=user)
        return AvailableSlot.objects.none()

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)


# ------------------------
# بیمار: رزرو تایم
# ------------------------
class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(patient=user)

    def perform_create(self, serializer):
        slot = serializer.validated_data["slot"]
        slot.is_booked = True
        slot.save()

        serializer.save(patient=self.request.user)
