from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
@admin.register(Image)
class ImagenAdmin(admin.ModelAdmin):
    pass

# Register your models here.
