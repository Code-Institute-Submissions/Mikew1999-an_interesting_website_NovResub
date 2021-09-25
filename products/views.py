from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Category
from .forms import ProductForm
from django.db.models import Q
from django.contrib.auth.models import User
from an_interesting_site import settings

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

    if 'author' in request.GET:
        author = request.GET['author']
        products = products.filter(author__in=author)

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
    ''' 
    A view to return a create and render the add product form 
    and handle users response
    '''
    categories_with_sizes = settings.categories_with_sizes
    print(categories_with_sizes)
    user = request.user
    user_id = None
    username = None
    form = ProductForm()
    file = 'No image'
    categories = Category.objects.all()
    category_list = []
    if user.is_authenticated:
        user_id = user.id
        username = user.username

    # Loops over the friendly names in categories model
    for category in categories:
        category_list.append(category.friendly_name)

    # If user is not logged in, re-direct user to login page
    # And show message telling user to login.
    if username == None:
        return redirect('account_login')

    # Handles form response
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            image = "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"
            title = form.cleaned_data['title']
            category_input = form.cleaned_data['category']
            category_object = Category(category_input)
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']

            rate = form.cleaned_data['rate']
            count = form.cleaned_data['count']
            has_sizes = form.cleaned_data['has_sizes']

            products = Products.objects.all()

            ids = []
            for x in products:
                ids.append(x.pk)

            new_id = int(ids[-1]) + 1

            print(f'New id = {new_id}')

            author = User(user_id)

            new_product = Products(title=title, image=image, category=category_input, price=price, description=description, rate=rate, count=count,
                                   has_sizes=has_sizes, author=author)

            new_product.save()

        return redirect('products')

    context = {
        'form': form,
        'category_list': category_list,
        'categories': categories,
        'user_id': user_id,
        'categories_with_sizes': categories_with_sizes,
    }

    return render(request, 'products/add_product.html', context)
