from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products
from products.views import products


# Create your views here.
def shopping_bag(request):
    ''' A view to return the shopping bag '''
    bag = request.session.get('bag', {})
    products = Products.objects.all()
    items = []

    for i in list(bag.keys()):
        items.append(i)

    products_in_bag = products.filter(pk__in=items)

    context = {
        'bag': bag,
        'products': products_in_bag,
    }
    return render(request, 'shopping_bag/shopping_bag.html', context)


def add_to_bag(request, item_id):
    ''' A view to add a product to the bag '''
    size = None
    product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST['quantity'])
    total = float(request.POST['tot'])
    redirect_url = request.POST['redirect_url']

    bag = request.session.get('bag', {})

    if 'size' in request.POST:
        size = request.POST['size']
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)