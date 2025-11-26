from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'summary', 'content', 'thumbnail',
            'category', 'created_by', 'is_active', 'created_at', 'updated_at'
        ]