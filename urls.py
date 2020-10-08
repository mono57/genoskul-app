from django.urls import path
from blog.views import PostListView, PostDetailView, CategoryDetailView

app_name = 'blog'

urlpatterns = [
    path(
        'posts/', 
        PostListView.as_view(), 
        name="post-list"),

    path(
        'posts/<int:pk>/details/', 
        PostDetailView.as_view(), 
        name="post-details"),

    path(
        'categories/<int:pk>/details/', 
        CategoryDetailView.as_view(), 
        name='category-detail')
]
