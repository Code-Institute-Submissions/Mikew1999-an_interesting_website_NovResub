from django.shortcuts import render, redirect


def checkout(request):
    ''' A view to return the checkout screen '''
    bag = request.session.get('bag', {})
    user = request.user
    delivery_details = False
    delivery_cost = None

    if bag == {}:
        return redirect('shopping_bag')

    if request.POST:
        if 'delivery' in request.POST:
            delivery_cost = request.POST['delivery']
        if 'address_1' in request.POST:
            address_1 = request.POST['address_1']
            address_2 = None
            if 'address_2' in request.POST:
                address_2 = request.POST['address_2']
            email = request.POST['email']
            post_code = request.POST['post_code']
            delivery_details = [address_1, address_2, post_code, email]
            return redirect('bank_details')

    context = {
        'user': user,
        'delivery_details': delivery_details,
        'delivery_cost': delivery_cost,
    }

    return render(request, 'checkout/checkout.html', context)


def bank_details(request):
    ''' A view to return billing details form '''
    bag = request.session.get('bag', {})
    if bag == {}:
        return redirect('shopping_bag')
    return render(request, 'checkout/bank_details.html')