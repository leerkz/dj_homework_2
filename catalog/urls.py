from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomePageView, ContactPageView, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
from django.urls import path, include

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('product_info/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('home/', ProductListView.as_view(), name='product_list'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
]
