from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User

# فرم ایجاد کاربر
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role')

# فرم تغییر کاربر
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'is_superuser', 'groups')

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('username', 'first_name', 'last_name', 'role', 'get_groups', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2', 'is_staff', 'is_superuser', 'groups'),
        }),
    )

    @admin.display(description='Groups')
    def get_groups(self, obj):
        return ", ".join([g.name for g in obj.groups.all()])
