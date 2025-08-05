from django.db import models 
from django.core.validators import FileExtensionValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(
        verbose_name= 'Icono',
        upload_to= 'categories/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','webp','ico'])],
        blank=True,
        null=True
    )
    class Meta:
        db_table = "categories"
        verbose_name ='Categoria'
        verbose_name_plural = 'Categorias'
        
    def delete(self,*args, **kwargs):
        if self.icon:
            self.icon.delete()
        super().delete(*args,**kwargs)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "products"
        verbose_name = "Producto"
        verbose_name_plural = "Productos" 

    def __str__(self):
        return f'nombre: {self.name} precio: {self.price}'
    
class Image(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        verbose_name='Imagen',
        upload_to= 'products/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','webp'])],
        blank=True,
        null=True
    )
    class Meta:
        db_table = "images"
        verbose_name ='Imagen'
        verbose_name_plural = 'Imagenes'
        
    def delete(self,*args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args,**kwargs)

    def __str__(self):
        return f"Imagen de {self.product.name}"