from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products
from products.views import products


# Create your views here.
def shopping_bag(request):
    ''' A view to return the shopping bag '''
    bag = request.session.get('bag', {})
    products = None
    items = []
    total = 0

    for product_id, product_data in bag.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Products, pk=product_id)
            product_price = float(product.price)
            product_total = product_price * product_data
            total += product_total
            size = None
            items.append({
                'product_id': product_id,
                'quantity': product_data,
                'product_total': product_total,
                'product': product,
                'price': product_price,
                'size': size,
            })
            products = True
        else:
            product = get_object_or_404(Products, pk=product_id)
            for size, quantity in product_data['items_by_size'].items():
                product_price = float(product.price)
                product_total = product_price * quantity
                total += product_total
                items.append({
                    'product_id': product_id,
                    'quantity': quantity,
                    'product': product,
                    'product_total': product_total,
                    'price': product_price,
                    'size': size
                })

    context = {
        'items': items,
        'products': products,
        'total': total
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