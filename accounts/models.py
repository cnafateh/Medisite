# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Roles(models.TextChoices):
        DOCTOR = "doctor", _("Doctor")
        EDITOR = "editor", _("Editor")
        PATIENT = "patient", _("Patient")

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        null=True,
        blank=True,
        help_text="کاربر چه نقشی دارد (Doctor / Editor / Patient)."
    )

    def is_doctor(self):
        return self.role == self.Roles.DOCTOR or self.is_superuser

    def is_editor(self):
        return self.role == self.Roles.EDITOR or self.is_superuser

    def is_patient(self):
        return self.role == self.Roles.PATIENT
