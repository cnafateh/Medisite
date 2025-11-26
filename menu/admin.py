# menu/admin.py
from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'is_visible', 'order')
    list_filter = ('is_visible',)
