from django.urls import path
from learning.views import *

app_name = 'learning'

urlpatterns = [
     path('document/create/',
          DocumentCreateView.as_view(),
          name='document'),
     path('list/',
         DocumentListView.as_view(), name='document-list'),   

     path('doc_categories/list/',
         DocumentCategoryListView.as_view(),
         name='doc_category-list'),
     path('documents/<int:pk>/detail/',
         CategoryDetailView.as_view(), name='category-detail'),
    
     path('courses/', CourseListView.as_view(), name='course-list')
   

]
