from django.urls import path
from django.contrib.auth.decorators import login_required
from users import views

urlpatterns=[route='signup/', view=views.Signupview.as_view(), name='signup'),
    
]