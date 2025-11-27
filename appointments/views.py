from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from django.db.models import Q
from django.utils import timezone

from .models import AvailableSlot, Appointment
from .serializers import SlotSerializer, AppointmentCreateSerializer, AppointmentSerializer


class AvailableSlotListAPI(generics.ListAPIView):
    """    
    Description: 
    Get all available time slots for appointments. 
    You can filter the results by date using the parameter `date=YYYY-MM-DD`.

    """
    serializer_class = SlotSerializer

    def get_queryset(self):
        qs = AvailableSlot.objects.filter(is_booked=False, end_time__gte=timezone.now())
        date = self.request.query_params.get("date")
        if date:
            # filter slots whose start_time date == date
            qs = qs.filter(start_time__date=date)
        return qs


class AppointmentCreateAPI(generics.GenericAPIView):
    """
    Description: 
    Create a new appointment using the form data. 
    Steps:
    1. Convert the preferred date and time from the form.
    2. Find an available slot where the preferred time fits (start <= dt < end) and it is not booked.
    3. Lock the slot in a transaction (select_for_update). If the slot is still free, the appointment is created.

    """
    serializer_class = AppointmentCreateSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        preferred_dt = data["preferred_datetime"]

        # پیدا کردن اسلات مناسب
        # شرط: start_time <= preferred_dt < end_time
        # همچنین is_booked=False
        slot_qs = AvailableSlot.objects.select_for_update().filter(
            start_time__lte=preferred_dt,
            end_time__gt=preferred_dt,
            is_booked=False
        ).order_by("start_time")

        if not slot_qs.exists():
            return Response(
                {"detail": "در زمان انتخاب‌شده اسلات آزاد موجود نیست. لطفاً زمان دیگری انتخاب کنید."},
                status=status.HTTP_409_CONFLICT
            )

        slot = slot_qs.first()

        # دوباره safety check (select_for_update تضمین کننده است)
        if slot.is_booked:
            return Response({"detail": "این اسلات هم‌اکنون رزرو شده است."}, status=status.HTTP_409_CONFLICT)

        # ساخت Appointment و ست کردن slot.is_booked
        appointment = Appointment.objects.create(
            first_name=data["first_name"],
            last_name=data["last_name"],
            phone=data.get("phone", ""),
            age=data.get("age"),
            preferred_datetime=preferred_dt,
            description=data.get("description", ""),
            slot=slot,
            status=Appointment.STATUS_PENDING
        )

        # mark slot as booked
        slot.is_booked = True
        slot.save()

        out_serializer = AppointmentSerializer(appointment)
        return Response(out_serializer.data, status=status.HTTP_201_CREATED)
