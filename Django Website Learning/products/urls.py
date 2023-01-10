from django.contrib import admin
from django.urls import path 

from products.views import view_all_products, dynamic_lookup_view #,delete_from_database, productDetailView, productCreateView, 

app_name = 'products'
urlpatterns = [
    path('', view_all_products),
    path('<int:id>/', dynamic_lookup_view, name="view-product"),
]
