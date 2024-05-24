from django.urls import path

from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail')
]
