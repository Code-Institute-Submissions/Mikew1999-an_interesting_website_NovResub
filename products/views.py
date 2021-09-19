from django.shortcuts import render
from .models import Products, Category


def products(request):
    ''' A view to show all products '''
    products = Products.objects.all()
    category_list = Category.objects.all()
    selected = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            selected = categories

    context = {
        'products': products,
        'categories': category_list,
        'selected': selected,
    }

    return render(
                    request,
                    'products/products.html',
                    context
                )
