
from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction, OperationalError
from django.utils import timezone
from .models import AvailableSlot, Appointment
from .serializers import SlotSerializer, AppointmentCreateSerializer, AppointmentSerializer
import time


class AvailableSlotListAPI(generics.ListAPIView):
    serializer_class = SlotSerializer

    def get_queryset(self):
        qs = AvailableSlot.objects.filter(is_booked=False, end_time__gte=timezone.now())
        date = self.request.query_params.get("date")
        if date:
            qs = qs.filter(start_time__date=date)
        return qs


class AppointmentCreateAPI(generics.GenericAPIView):
    serializer_class = AppointmentCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        preferred_dt = data["preferred_datetime"]

        for attempt in range(3):
            try:
                with transaction.atomic():

                    slot_qs = AvailableSlot.objects.select_for_update().filter(
                        start_time__lte=preferred_dt,
                        end_time__gt=preferred_dt
                    ).order_by("start_time")

                    if not slot_qs.exists():
                        return Response({"detail": "اسلاتی در این زمان وجود ندارد."}, status=409)

                    slot = slot_qs.first()

                    if slot.is_booked:
                        return Response({"detail": "این اسلات رزرو شده است."}, status=409)

                    slot.is_booked = True
                    slot.save(update_fields=["is_booked"])

                    appointment = Appointment.objects.create(
                        first_name=data.get("first_name"),
                        last_name=data.get("last_name"),
                        phone=data.get("phone", ""),
                        age=data.get("age"),
                        preferred_datetime=preferred_dt,
                        description=data.get("description", ""),
                        slot=slot,
                        status=Appointment.STATUS_PENDING
                    )

                    out = AppointmentSerializer(appointment)
                    return Response(out.data, status=201)

            except OperationalError as e:
                if "lock" in str(e).lower():
                    time.sleep(0.3)
                    continue
                raise e

        return Response({"detail": "سیستم شلوغ است، دوباره تلاش کنید."}, status=503)
