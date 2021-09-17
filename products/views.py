from django.shortcuts import render
from .models import Products, Category


def products(request):
    ''' A view to show all products '''
    products = Products.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(
                    request,
                    'products/products.html',
                    context
                )
