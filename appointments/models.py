from django.db import models


class AvailableSlot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_time"]
        unique_together = ("start_time", "end_time")

    def __str__(self):
        return f"{self.start_time.isoformat()} → {self.end_time.isoformat()}"


class Appointment(models.Model):
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELLED = "cancelled"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    # اطلاعات بیمار (بدون حساب کاربری)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)

    # زمانی که بیمار درخواست کرده (برای لاگ و اطلاع)
    preferred_datetime = models.DateTimeField(null=True, blank=True)

    # نوبت رزروشده (هر اسلات فقط یک appointment دارد)
    slot = models.OneToOneField(
        AvailableSlot,
        on_delete=models.CASCADE,
        related_name="appointment"
    )

    description = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.slot}"
