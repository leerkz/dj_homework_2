from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy, reverse


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_post_list.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'
    context_object_name = 'blog_post'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_post_form.html'

    def get_success_url(self):
        return reverse('blog:blog_post_detail', kwargs={'pk': self.object.pk})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_post_form.html'
    success_url = reverse_lazy('blog:blog_post_list')

    def get_success_url(self):
        return reverse('blog:blog_post_detail', args=[self.kwargs.get('pk')])



class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_post_list')
