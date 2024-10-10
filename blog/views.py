from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        obj = super().get_object
        if obj.is_active:
            obj.views += 1
            return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published', 'view_counter')
    template_name = "test"
    success_url = reverse_lazy('test')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    success_url = reverse_lazy('blog:blog_list')
