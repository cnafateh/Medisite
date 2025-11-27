from django.urls import path
from .views import AvailableSlotListAPI, AppointmentCreateAPI

urlpatterns = [
    path("slots/", AvailableSlotListAPI.as_view(), name="slots-list"),
    path("book/", AppointmentCreateAPI.as_view(), name="appointment-create"),
]
