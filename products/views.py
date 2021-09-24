from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Category
from .forms import ProductForm
from django.db.models import Q

form = ProductForm()


def products(request):
    ''' A view to show all products '''
    sort = 'title'
    products = Products.objects.all().order_by(sort)
    category_list = Category.objects.all()
    selected = None
    search = None
    username = None
    user = request.user
 
    if user.is_authenticated:
        username = request.user.username


    if request.GET:
        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            products = products.filter(category__name__in=categories)
            selected = ', '.join(categories)

        if 'q' in request.GET:
            search = request.GET['q']
            results = Q(title__icontains=search) | Q(
                category__name__icontains=search)
            products = products.filter(results)
            selected = str(search)

        if 'sort' in request.GET:
            sort = request.GET['sort']
            products = Products.objects.all().order_by(sort)

    context = {
        'products': products,
        'categories': category_list,
        'selected': selected,
        'sort': sort,
        'username': username,
    }

    return render(
        request,
        'products/products.html',
        context
    )


def productdetails(request, product_id):
    ''' A view to return details of the specified product '''
    product = get_object_or_404(Products, pk=product_id)
    price = product.price

    context = {
        'product': product,
        'price': price,
    }

    return render(request, 'products/product_details.html', context)


def add_product(request):
    ''' A view to return a create product form '''
    username = None
    user = request.user
    file = 'No image'
    categories = Category.objects.all()
    category_list = []

    for category in categories:
        category_list.append(category.friendly_name)
 
    if user.is_authenticated:
        username = request.user.username

    if username == None:
        return redirect('account_login')


    if request.POST:
        if request.FILES:
            file = request.FILES['image']

        title = request.POST['title']
        category = request.POST['category']
        price = request.POST['price']
        description = request.POST['description']
        rate = None
        count = None
        print(f'Title: {title}, Description: {description}, Price: {price}, Category: {category}, Username: {username}, Image: {file} ')

    context = {
        'form': form,
        'username': username,
        'category_list': category_list,
        'categories': categories,
    }

    return render(request, 'products/add_product.html', context)