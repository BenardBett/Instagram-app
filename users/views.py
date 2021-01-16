from django.shortcuts import render
from django.contrib.auth import logout
from users.forms import SignupForm
from posts.models import Post
from users.models import Profile
# Create your views here.

class SignupView(FormView):
    """Signup View."""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """If the form is valid save the user"""
        form.save()
        return super().form_valid(form)
    
    class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'users/login.html'
    redirect_authenticated_user = True