from django.db import models
from django.utils.timezone import localtime

class AvailableSlot(models.Model):
    start_time = models.DateTimeField(db_index=True)
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_time"]
        indexes = [
            models.Index(fields=['start_time', 'end_time']),
            models.Index(fields=['is_booked', 'start_time']),
        ]


    def __str__(self): return f"{str(localtime(self.start_time))[0:11]} -> {str(localtime(self.start_time))[11:16]} - {str(localtime(self.end_time))[11:16]}"
class Appointment(models.Model):
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    preferred_datetime = models.DateTimeField(null=True, blank=True)
    slot = models.OneToOneField(AvailableSlot, on_delete=models.CASCADE, related_name="appointment")
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.slot}"

