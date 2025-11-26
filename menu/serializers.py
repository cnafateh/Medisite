from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'title', 'url', 'parent', 'is_visible', 'order', 'children']

    def get_children(self, obj):
        qs = obj.children.all()
        return MenuSerializer(qs, many=True).data
