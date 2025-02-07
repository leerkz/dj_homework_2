from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.models import Product
from blog.models import BlogPost
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем владельца
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:product_info", args=[self.object.pk])


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class HomePageView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ContactPageView(TemplateView):
    template_name = 'contacts.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_info.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
