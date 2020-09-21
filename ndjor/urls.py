from django.urls import path

from ndjor.views import ProductListView


app_name = 'ndjor'

urlpatterns = [
    path(
        'product/list/',
        ProductListView.as_view(), 
        name='product-list'),
    
]
