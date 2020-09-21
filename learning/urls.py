from django.urls import path

from learning.views import *

app_name = 'learning'

urlpatterns = [
    # path(
    #     'document/create/',
    #     DocumentCreateView.as_view(),
    #     name='document-create'),
        
    path('document/list/',
         DocumentListView.as_view(),
         name='document-list'),
        
    path('document/categories/list/',
    DocumentCategoryListView.as_view(), name='doc_category-list')

]
