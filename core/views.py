from django.shortcuts import render
from django.views import View
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
#-------------------------------------------------------------------#
#  Index View
#-------------------------------------------------------------------#
class IndexView(View): 
    template_name = 'index.html'
    
    def get(self,request, *args, **kwargs):
        categories= Category.objects.all()
        products= Product.objects.order_by("-created_at")[:9]
        products_imagen= []
        for product in products: 
            image= product.image_set.filter(is_main=True).first()
            if not image:
                image= product.image_set.first()
            products_imagen.append({"product":product,"image":image}) 
        context= {'categories':categories,"products": products_imagen}
        print(categories)
        print(products)
        return render(request, self.template_name,context)
    
#-------------------------------------------------------------------#
#  Product View
#-------------------------------------------------------------------#
class ProductsView(View): 
    template_name = 'paginas/productos.html'

    paginate_by= 1
    
    def get(self,request, *args, **kwargs):
        query= request.GET.get('q')
        products = Product.objects.all()
        if query:
            products = products.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        products_imagen= []
        for product in products: 
            image= product.image_set.filter(is_main=True).first()
            if not image:
                image= product.image_set.first()
            products_imagen.append({"product":product,"image":image})

        paginator = Paginator(products_imagen, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        print(page_obj)

        context= {
            "page_obj": page_obj,
            "products": page_obj.object_list,
            "query": query
            }
        return render(request, self.template_name,context)

#-------------------------------------------------------------------#
#  Login View
#-------------------------------------------------------------------#
class LoginView(View): 
    template_name = 'paginas/login.html'
    
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    
#-------------------------------------------------------------------#
#  Register View
#-------------------------------------------------------------------#
class RegisterView(View): 
    template_name = 'paginas/register.html'
    
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)