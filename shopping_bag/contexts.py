''' Required django import '''
from django.shortcuts import get_object_or_404
from products.models import Products


# context inspired from code institue walkthrough project
def bag_items(request):
    ''' Defines the contents of users shopping bag '''
    bag = request.session.get('bag', {})
    products = None
    items = []
    total = 0

    for product_id, product_data in bag.items():
        # If item doesn't have size
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
            # If item has size
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
                products = True

    context = {
        'items': items,
        'products': products,
        'total': total
    }

    return context


def delivery(request):
    ''' Defines Delivery costs '''
    context = {
        'standard_delivery': 5,
        'next_day_delivery': 10,
    }

    return context
