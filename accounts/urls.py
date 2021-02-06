from django.urls import path, include
from accounts.views import *


app_name = 'accounts'

urlpatterns = [
    #path('', include('templates.urls')),
    path('profile/update/', RegisterStep1.as_view(),name='register-step2'),
    path('register/', SignupView.as_view(), name='register'),
    path('user/<int:pk>/update/', UserInfoUpdateView.as_view(), name='user_info-update'),
]
