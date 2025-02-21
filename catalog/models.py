from django.db import models

from users.models import CustomUser


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя продукта')
    description = models.TextField(verbose_name='Описание продукта', null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', blank=True)
    category = models.CharField(max_length=150, verbose_name='Категория', blank=True)
    cost = models.FloatField(verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    publication_status = models.BooleanField(default=False, verbose_name='статус публикации', blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'description', 'category', 'cost']
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя продукта')
    description = models.TextField(verbose_name='Описание продукта', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', 'description']
