from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from catalog.models import Product
from blog.models import BlogPost
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_initial(self):
        initial = super().get_initial()
        initial["owner"] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("product.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied

    def test_func(self):
        return self.request.user == self.get_object().owner

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied
        return redirect('catalog:product_list')


class HomePageView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ContactPageView(TemplateView):
    template_name = 'contacts.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()  # Получаем объект Product
        context['product_name'] = product.name
        context['product_description'] = product.description
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ProductModeratorsView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("У вас нет прав доступа на удаление")

        product.delete()

        return redirect('catalog:product_list')

    def test_func(self):
        return self.request.user == self.get_object().owner

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied
        return redirect('catalog:product_list')
