from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)  # لینک مقصد
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="children"
    )
    is_visible = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # مرتب‌سازی بر اساس order
