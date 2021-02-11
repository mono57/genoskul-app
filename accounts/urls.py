from django.urls import path, include
from accounts.views import *


app_name = 'accounts'

urlpatterns = [
    #path('', include('templates.urls')),
    path('profile/completion/', ProfileCompletionUpdateView.as_view(),
         name='profile-completion'),
    path('register/', SignupView.as_view(), name='register'),
    path('user/<int:pk>/update/', UserInfoUpdateView.as_view(),
         name='user_info-update'),
]
