from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import Product, Category


class CategoryProductsView(ListView):
    model = Product
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        return Product.objects.filter(category=category_name, publication_status=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs.get('category_name')
        context['category'] = get_object_or_404(Category, name=category_name)
        return context
