from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, contacts
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('contacts', contacts),
    path('catalog/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/update', ProductUpdateView.as_view(), name='product_update'),
]
