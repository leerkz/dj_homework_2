from django.shortcuts import render
from catalog.models import Product, Category


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product_name': product.name,
        'product_description': product.description,
        'product_image': product.image,
        'product_category': product.category,
        'product_cost': product.cost,
        'product_created_at': product.created_at,
        'product_updated_at': product.updated_at

    }
    return render(request, template_name='product_info.html', context=context)


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'home.html', context=context)