from django.urls import path

from dashboard.views import *
from accounts.views import ProfileUpdateView
from ndjor.views import ProductCreateView, ProductUpdateView
from learning.views import DocumentCreateView
# from jobs.views import

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name='dashboard'),
    path('documents/',
         DashboardDocumentListView.as_view(),
         name='documents'),
    path('document/create/',
         DocumentCreateView.as_view(),
         name='document-create'),

    path('document/<int:pk>/delete/',
         DashboardDocumentDeleteView.as_view(),
         name='document-delete'),

    path('products/<int:pk>/delete/',
         DashboardProductDeleteView.as_view(),
         name='product-delete'),

    path('jobs/create/',
         DashboardJobCreateView.as_view(),
         name='job-create'),

    path('job/<int:pk>/update/',
         DashboardJobUpdateView.as_view(),
         name='job-update'),

    path('jobs/list/',
         DashboardJobsListView.as_view(),
         name='jobs-list'),

    path('resume/add/',
         DashboardResumeCreateView.as_view(),
         name='resume-create'),

    path('resume/<int:pk>/update/',
         DashboardResumeUpdateView.as_view(),
         name='resume-update'),

    path('product/create/',
         ProductCreateView.as_view(),
         name='product-create'),

    path('product/<int:pk>/update/',
         ProductUpdateView.as_view(),
         name='product-update'),

    path('services/create/',
         DashboardServiceCreateView.as_view(),
         name='service-create'),

    path('product/list/',
         DashboardProductListView.as_view(),
         name='products'),

    path('profile/update/',
         ProfileUpdateView.as_view(),
         name='profile-update'),
]
