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
    
    
    def get_context_data(self, **kwargs):
        """Add User and profile to context."""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context
    
class PostFeedView(ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 4
    context_object_name = 'posts'

