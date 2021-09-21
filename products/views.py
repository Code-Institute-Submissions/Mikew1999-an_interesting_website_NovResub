from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Products, Category
from django.db.models import Q


def products(request):
    ''' A view to show all products '''
    sort = 'title'
    products = Products.objects.all().order_by(sort)
    category_list = Category.objects.all()
    selected = None
    search = None
    users = User.objects.all()

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
        'users': users,
    }

    return render(
        request,
        'products/products.html',
        context
    )


def productdetails(request, product_id):
    ''' A view to return details of the specified product '''
    product = get_object_or_404(Products, pk=product_id)
    users = User.objects.all()

    if 'sessionid' in request.session:
        print("hello")
    context = {
        'product': product,
        'users': users
    }

    return render(request, 'products/product_details.html', context)
