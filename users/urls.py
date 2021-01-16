from django.urls import path
from django.contrib.auth.decorators import login_required
from users import views

urlpatterns=[route='signup/', view=views.Signupview.as_view(), name='signup'),
urlpatterns=[route='login/', view=views.Loginview.as_view(), name='login'),
urlpatterns=[route='logout/', view=views.Logout.as_view(), name='logout'), 
urlpatterns=[route='me/profile/', view=views.UpdateProfile.as_view(), name='update_profile'), 
urlpatterns=[route='<str:username_slug>/', view=login_required(views.UserDetailView.as_view()), name='detail'), 
]