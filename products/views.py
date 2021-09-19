from django.shortcuts import render
from .models import Products, Category
from django.db.models import Q


def products(request):
    ''' A view to show all products '''
    products = Products.objects.all()
    category_list = Category.objects.all()
    selected = None
    search = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            products = products.filter(category__name__in=categories)
            selected = ', '.join(categories).capitalize()

        if 'q' in request.GET:
            search = request.GET['q']
            results = Q(title__icontains=search) | Q(
                category__name__icontains=search)
            products = products.filter(results)
            selected = str(search)

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
