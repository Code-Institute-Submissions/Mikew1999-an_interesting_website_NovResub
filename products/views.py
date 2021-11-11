''' Required imports '''
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from reviews.calculate_reviews import CalculateRating
from reviews.models import Review
from .models import Products, Category, Likes
from .forms import ProductForm


def products(request):
    ''' A view to show all products '''
    # Initial sorting
    sort = 'rate'
    # Initial number of products to show
    num_of_products = 15
    # List of products
    product_list = Products.objects.all().order_by(sort)[:15]
    # List of all categories
    category_list = Category.objects.all()
    # Initialising variables
    selected = None
    search = None
    username = None
    user = request.user
    likes = Likes.objects.all()
    users_liked_products = []

    if request.POST:
        # Category drop down form handling
        if 'category' in request.POST:
            selected_option = str(request.POST['category'])
            if selected_option == 'clothing':
                categories = ['mens_clothing', 'womens_clothing']
                selected = categories
            elif selected_option == 'home_garden':
                categories = ['home', 'garden']
                selected = categories
            else:
                categories = selected_option
                selected = categories

            # Shows list of all
            product_list = Products.objects.filter(category__name__in=categories)

    for product in product_list:
        CalculateRating(product_id=product.pk)

    if user.is_authenticated:
        username = request.user.username
        for item in likes:
            if item.user.id == user.id:
                users_liked_products.append(item.product.pk)

    if 'author' in request.GET:
        author = request.GET['author']
        product_list = product_list.filter(author__in=author)

    if request.GET:
        if 'q' in request.GET:
            search = request.GET['q'].strip()
            results = Q(title__icontains=search) | Q(
                category__name__icontains=search)
            product_list = product_list.filter(results)
            selected = str(search)

        if 'sort' in request.GET:
            sort = request.GET['sort']
            product_list = Products.objects.all().order_by(sort)

    context = {
        'products': product_list,
        'categories': category_list,
        'selected': selected,
        'sort': sort,
        'username': username,
        'likes': likes,
        'users_liked_products': users_liked_products,
    }

    return render(
        request,
        'products/products.html',
        context
    )


def productdetails(request, product_id):
    ''' A view to return details of the specified product '''
    form = ProductForm()
    product = get_object_or_404(Products, pk=product_id)
    price = product.price
    reviews = Review.objects.filter(product_id=product_id)

    context = {
        'product': product,
        'price': price,
        'reviews': reviews,
    }

    return render(request, 'products/product_details.html', context)


def add_product(request):
    '''
    A view to return a create and render the add product form
    and handle users response
    '''
    user = request.user
    user_id = None
    username = None
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
    if username is None:
        return redirect('account_login')

    # Handles form response
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            image = "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"
            title = form.cleaned_data['title']
            category_input = form.cleaned_data['category']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']

            rate = form.cleaned_data['rate']
            count = form.cleaned_data['count']
            has_sizes = form.cleaned_data['has_sizes']

            author = User(user_id)

            new_product = Products(
                            title=title, image=image,
                            category=category_input, price=price,
                            description=description, rate=rate,
                            count=count, has_sizes=has_sizes, author=author)

            new_product.save()

        return redirect('products')

    context = {
        'form': form,
        'category_list': category_list,
        'categories': categories,
        'user_id': user_id,
    }

    return render(request, 'products/add_product.html', context)


def like(request, product_id, user_id):
    ''' Likes a product '''
    product = Products(product_id)
    user = User(user_id)
    new_like = Likes(product=product, user=user)
    new_like.save()
    return redirect(request, 'products')


def unlike(request, product_id, user_id):
    ''' Unlikes a product '''
    item = Likes.objects.filter(
        user=User(user_id)).filter(product=Products(product_id))
    item.delete()
    return redirect(request, 'products')
