from django.urls import path
from .views import (
    AvailableSlotListCreateAPIView,
    AppointmentListCreateAPIView
)

urlpatterns = [
    path("slots/", AvailableSlotListCreateAPIView.as_view(), name="slot-list"),
    path("appointments/", AppointmentListCreateAPIView.as_view(), name="appointment-list"),
]
