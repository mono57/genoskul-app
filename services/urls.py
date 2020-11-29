from django.urls import path

from services.views import *

app_name = 'services'

urlpatterns = [
    path('<int:pk>/detail/', BoxDetailView.as_view(), name='box-detail'),

   
    
]
