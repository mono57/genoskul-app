from django.urls import path

from jobs.views import *

app_name = 'jobs'

urlpatterns = [
    path('list/',
         JobListView.as_view(), name='job-list'),
    path('resumes/list/', ResumeListView.as_view(), name='resume-list'),
    path('resumes/<int:pk>/detail/', ResumeDetailView.as_view(), name='resume-detail'),
    path('<int:pk>/detail/', JobDetailView.as_view(), name='job-detail'),
]
