from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from posts.models import Post
from posts.forms import PostForm


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create New Post View"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    context_object_name = 'form'