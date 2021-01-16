from django.urls import path
from django.contrb.auth.decorators import login_required
from posts import views

urlpatterns = [
    path(
        route='',
        view=login_required(views.PostFeedView.as_view()),
        name='feed'
    ),
     path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create_post'
    ),
]