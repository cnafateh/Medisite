# blog/admin.py
from django.contrib import admin
from .models import Category, Post

# Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'created_by')
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

# Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'created_at', 'updated_at', 'created_by')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('is_active', 'category', 'created_by')
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)