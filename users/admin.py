from django.contrib import admin

from users.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class Product(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'avatar',)
    list_filter = ('email',)
