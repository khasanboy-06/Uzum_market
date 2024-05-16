from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import CreateProduct

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', context={"products":products, "cats":categories})


def category(request, id):
    cat = get_object_or_404(Category, id=id)
    products = cat.products.all()
    categories = Category.objects.all()
    return render(request, 'home.html', context={"products":products, "cats":categories})


def batafsil(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    return render(request, 'batafsil.html', context={"product":product, "cats":categories})


def create_product(request):
    form = CreateProduct()
    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/')
        return render(request, 'create_product.html', context={"form":form})
    

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/')


def update_product(request, id):
    product = get_object_or_404(Product, id=id)

    form = CreateProduct(instance=product)
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()

            return redirect('/')

    return render(request, 'create_product.html', context={"form":form})
