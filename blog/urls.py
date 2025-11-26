from django.urls import path
from .views import CategoryListAPIView, CategoryRetrieveAPIView, PostListAPIView, PostRetrieveAPIView


urlpatterns = [
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryRetrieveAPIView.as_view(), name="category-detail"),
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostRetrieveAPIView.as_view(), name="post-detail"),
]
