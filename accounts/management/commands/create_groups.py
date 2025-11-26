# accounts/management/commands/create_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# مدل‌هایی که پرمیشن‌ها برای آن‌ها لازم است
from blog.models import Post, Category
from core.models import DoctorProfile
from appointments.models import AvailableSlot, Appointment
from menu.models import Menu

class Command(BaseCommand):
    help = "Create default groups (Doctor, Editor, Patient) and assign basic permissions."

    def handle(self, *args, **options):
        # 1) Doctor group
        doctor_group, created = Group.objects.get_or_create(name="Doctor")
        self.stdout.write(f"Doctor group {'created' if created else 'exists'}")

        # Doctor: full control on blog (view/change/add/delete), doctorprofile, appointments slots view/add/change, menu manage
        # جمع کردن permissions مرتبط
        perms = []
        for model in (Post, Category):
            ct = ContentType.objects.get_for_model(model)
            perms += list(Permission.objects.filter(content_type=ct))
        # DoctorProfile
        ct = ContentType.objects.get_for_model(DoctorProfile)
        perms += list(Permission.objects.filter(content_type=ct))
        # Appointments (AvailableSlot, Appointment)
        for model in (AvailableSlot, Appointment):
            ct = ContentType.objects.get_for_model(model)
            perms += list(Permission.objects.filter(content_type=ct))
        # Menu
        ct = ContentType.objects.get_for_model(Menu)
        perms += list(Permission.objects.filter(content_type=ct))

        doctor_group.permissions.set(perms)
        self.stdout.write("Doctor permissions assigned")

        # 2) Editor group
        editor_group, created = Group.objects.get_or_create(name="Editor")
        self.stdout.write(f"Editor group {'created' if created else 'exists'}")

        # Editors: can add/view posts and categories; change/delete limited via admin checks (we'll enforce edit ownership in admin).
        editor_perms = []
        for model in (Post, Category):
            ct = ContentType.objects.get_for_model(model)
            # only add, view, change (we'll restrict change/delete in admin override)
            editor_perms += list(Permission.objects.filter(content_type=ct, codename__in=['add_'+model.__name__.lower(), 'view_'+model.__name__.lower(), 'change_'+model.__name__.lower()]))
        editor_group.permissions.set(editor_perms)
        self.stdout.write("Editor permissions assigned")

        # 3) Patient group
        patient_group, created = Group.objects.get_or_create(name="Patient")
        self.stdout.write(f"Patient group {'created' if created else 'exists'}")
        # Patients: no admin permissions; API permissions handle access
        patient_group.permissions.clear()

        self.stdout.write("Groups setup complete.")
