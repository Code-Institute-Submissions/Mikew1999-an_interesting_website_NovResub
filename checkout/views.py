from django.shortcuts import render, redirect


def checkout(request):
    ''' A view to return the checkout screen '''
    bag = request.session.get('bag', {})
    user = request.user
    delivery_details = False

    if bag == {}:
        return redirect('shopping_bag')

    if request.POST:
        if 'address_1' in request.POST:
            address_1 = request.POST['address_1']
            address_2 = None
            if 'address_2' in request.POST:
                address_2 = request.POST['address_2']
            email = request.POST['email']
            post_code = request.POST['post_code']
            delivery_details = [address_1, address_2, post_code, email]

    context = {
        'user': user,
        'delivery_details': delivery_details,
    }

    return render(request, 'checkout/checkout.html', context)