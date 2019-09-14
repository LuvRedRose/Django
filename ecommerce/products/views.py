from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
# from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import ProductForm
from .models import ProductModel

#@login_required
def index(request):
    products = ProductModel.objects.all()
    page  = request.GET.get('page', 1)
    paginator = Paginator(products, 1)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'Title' : 'List Product',
        'product' : products,
    }

    return render(request, 'products/index.html', context)


def AddProduct(request):
    
    error = None
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES or None)
        if product_form.is_valid():
            product_form.save()
            return redirect('products:index')
    else:
        product_form = ProductForm()

    context = {
        'Title' : 'Add Product',
        'product_form' : product_form
    }

    return render(request, 'products/add_product.html', context)

def DeleteProduct(request, delete_id):
    ProductModel.objects.filter(id=delete_id).delete()
    return redirect('products:index')

def UpdateProduct(request, update_id):
    product_update = ProductModel.objects.get(id=update_id)

    data  = {
        'product_name'     : product_update.product_name,
        'detail'           : product_update.detail,
        'category'         : product_update.category,
        'price'            : product_update.price,
        'quantity'         : product_update.quantity,
        'image'            : product_update.image,
    }

    product_form = ProductForm(request.POST, request.FILES or None, initial=data, instance=product_update)
    error = None 
    
    if request.method == 'POST':
        if product_form.is_valid():
            product_form.save()
            return redirect('products:index')
        else:
            product_form = ProductForm()

    context = {
        'Title' : 'Update Products',
        'product_form' : product_form,
    }

    return render(request, 'products/update_product.html', context)