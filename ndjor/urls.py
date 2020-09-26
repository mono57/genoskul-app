from django.urls import path

from ndjor.views import ProductListView, ProductCategoryDetailView


app_name = 'ndjor'

urlpatterns = [
    path(
        'product/list/',
        ProductListView.as_view(), 
        name='product-list'),

    path(
        'category/<int:pk>/details/',
        ProductCategoryDetailView.as_view(),
        name='category-details'
    )
    
]
