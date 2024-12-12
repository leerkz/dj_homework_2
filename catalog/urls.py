from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_info, product_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_info/<int:pk>/', product_info, name='product_info'),
    path('home', product_list, name='product_list')
]
