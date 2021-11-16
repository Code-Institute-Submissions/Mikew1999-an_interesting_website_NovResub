from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products
from products.views import products
from .contexts import bag_items


# Create your views here.
def shopping_bag(request):
    ''' A view to return the shopping bag '''
    bag = request.session.get('bag', {})
    bag_contents = bag_items(request)
    total = bag_contents['total']
    deal = bag_contents['deal']
    delivery_cost = request.session.get('delivery_cost', {})

    if deal == 'Free Delivery on all orders':
        delivery_cost['cost'] = 0
    elif total >= 50:
        delivery_cost['cost'] = 0

    if request.GET:
        # Clears bag
        if 'clear' in request.GET:
            request.session['bag'] = bag
            del request.session['bag']
            return redirect(shopping_bag)

    if request.POST:
        # set delivery details
        if 'delivery' in request.POST:
            delivery = request.POST['delivery']
            if delivery == 'Next Day':
                delivery_cost['cost'] = 10
            elif delivery == '3 - 5':
                delivery_cost['cost'] = 7
            else:
                delivery_cost['cost'] = 3

    request.session['delivery_cost'] = delivery_cost

    context = {
        'delivery_details': request.session['delivery_cost'],
        'total': total,
    }

    return render(request, 'shopping_bag/shopping_bag.html', context)


def add_to_bag(request, item_id):
    ''' A view to add a product to the bag '''
    size = None
    quantity = int(request.POST['quantity'])
    redirect_url = request.POST['redirect_url']

    bag = request.session.get('bag', {})

    if quantity < 1:
        return redirect('productdetails', product_id=item_id)

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


def amend_bag(request, item_id):
    ''' A view to handle amending the bag '''
    bag = request.session.get('bag', {})
    if request.POST:
        if 'quantity' in request.POST:
            quantity = int(request.POST['quantity'])

            if 'size' in request.POST:
                size = request.POST['size']
                bag[item_id]['items_by_size'][size] = quantity
                if quantity == 0:
                    del bag[item_id]['items_by_size'][size]
                    if bag[item_id]['items_by_size'] == {}:
                        bag.pop(item_id)

            else:
                if quantity == 0:
                    bag.pop(item_id)
                else:
                    bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect('shopping_bag')
