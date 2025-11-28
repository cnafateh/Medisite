from rest_framework import generics
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# ----------------------
# Categories Views
# ----------------------
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ----------------------
# Posts Views
# ----------------------
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(is_active=True).order_by('id')

class PostReverseListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(is_active=True).order_by('-id')

class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer