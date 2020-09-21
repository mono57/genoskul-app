from django.urls import path, include
from accounts.views import *


app_name = 'accounts'

urlpatterns = [
    # path('', include('allauth.urls')),
    path('step2/', RegisterStep1.as_view(),name='register-step2'),
    path('register/', SignupView.as_view(), name='register')
]
