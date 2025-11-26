from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(source='created_by', read_only=True)  
    author = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = [
            'id', 'title', 'slug', 'description', 'created_at', 'updated_at', 'author_id', 'author'
        ]

    def get_author(self, obj):
        user = obj.created_by
        if user:
            full_name = f"{user.first_name} {user.last_name}".strip()
            return full_name if full_name else user.username
        return None


class PostSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source='category', read_only=True)  
    category_name = serializers.StringRelatedField(source='category', read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='created_by', read_only=True)  
    author = serializers.SerializerMethodField()
    
    

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'summary', 'content', 'thumbnail',
            'category_id', 'category_name',
            'author_id', 'author',
            'is_active', 'created_at', 'updated_at'
        ]

    def get_author(self, obj):
        user = obj.created_by
        if user:
            full_name = f"{user.first_name} {user.last_name}".strip()
            return full_name if full_name else user.username
        return None


