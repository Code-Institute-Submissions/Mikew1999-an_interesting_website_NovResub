from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Category
from .forms import ProductForm
from django.db.models import Q
from django.contrib.auth.models import User

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
    user = request.user
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
        if request.FILES:
            file = request.FILES['image']
        image = None
        title = request.POST['title']
        category_input = request.POST['category']
        category_object = Category(category_input)
        price = request.POST['price']
        description = request.POST['description']
        rate = None
        count = None
        has_sizes = None

        products = Products.objects.all()
        ids = []
        for x in products:
            ids.append(x.id)

        last_id = ids[-1]

        author = User(user_id)

        p = Products(title=title, price=price, description=description,
                     rate=0, count=0, category=category_object, image=image,
                     has_sizes=has_sizes, author=author)
        p.save()

        return redirect('productdetails', product_id=p.pk)

    context = {
        'form': form,
        'category_list': category_list,
        'categories': categories,
    }

    return render(request, 'products/add_product.html', context)
