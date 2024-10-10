from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogPostCreateView, BlogPostDetailView, BlogPostUpdateView, BlogPostListView

app_name = BlogConfig.name

urlpatterns = [
    path('posts_list', BlogPostListView.as_view(), name='blog_posts_list'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='blog_post_details'),
    path('posts/create/', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('posts/update', BlogPostUpdateView.as_view(), name='blog_post_update')
]
