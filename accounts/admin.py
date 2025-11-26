from django.contrib import admin
from django.contrib.auth import get_user_model
from accounts.models import User

# User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
