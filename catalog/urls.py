from django.urls import path, include
from catalog.apps import CatalogConfig
from config import settings
from . import views
from catalog.views import product_list, product_details, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list),
    path('products/<int:pk>/', product_details, name='product_details'),
    path('contacts', contacts)
]
