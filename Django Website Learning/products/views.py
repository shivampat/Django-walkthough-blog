from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

def view_all_products(request):
    queryset = Product.objects.all()   
    content = {
        'objects': queryset,
    }
    return render(request, "products/product_view_all.html", content)

#def delete_from_database(request, id):
#    obj = get_object_or_404(Product, id=id)
#
#    if request.method == "POST":
#        obj.delete()
#        return redirect(f'/product/{id-1}/delete')
#        
#    content = {
#        'object': obj,
#    }
#    return render(request, "products/product_delete.html", content)

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    content = {
        'object': obj,
    }
    return render(request, "products/product_data.html", content)


#def productCreateView(request):
#    form = RawProductForm()
#    if request.method == 'POST':
#        form = RawProductForm(request.POST)
#        if form.is_valid():
#            print(form.cleaned_data)
#            Product.objects.create(**form.cleaned_data)
#        else:
#            print(form.errors)
#
#    content = {
#        'form': form
#    }
#    return render(request, "products/product_create.html", content)


#def productCreateView(request):
#    print(request.GET)
#    print(request.POST)
#    content = {}
#    return render(request, "products/product_create.html", content)

# def productCreateView(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
# 
#     content = {
#         'form': form,
#     }
#     return render(request, "products/product_create.html", content)

#def productDetailView(request):
#    obj = Product.objects.get(id=2)
#    content = {
#        'object': obj,
#    }
#    return render(request, "products/product_data.html", content)