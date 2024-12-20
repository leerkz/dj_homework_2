from catalog.apps import CatalogConfig

from blog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path('blog/', BlogPostListView.as_view(), name='blog_post_list'),
    path('blog/post/<int:pk>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog/post/new/', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog/post/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog/post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_post_delete'),

]