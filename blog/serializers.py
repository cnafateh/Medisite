from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(source='category', read_only=True)
    created_by_name = serializers.StringRelatedField(source='created_by', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'summary', 'content', 'thumbnail',
            'category', 'category_name',
            'created_by', 'created_by_name',
            'is_active', 'created_at', 'updated_at'
        ]