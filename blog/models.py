from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200, blank=True)
    preview = models.ImageField(upload_to='blog_previews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    views_count = models.PositiveIntegerField(default=0, blank=True)

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title
