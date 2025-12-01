from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Appointment, AvailableSlot

@receiver(post_delete, sender=Appointment)
def free_slot_when_appointment_deleted(sender, instance, **kwargs):
    if instance.slot:
        slot = instance.slot
        slot.is_booked = False
        slot.save(update_fields=["is_booked"])
