from django.urls import path
from blog.views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('posts/', PostListView.as_view(), name="post-list"),
    path('posts/<str:slug>/details/', PostDetailView.as_view(), name="post-details"),
]
