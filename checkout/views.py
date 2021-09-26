from django.shortcuts import render, redirect


def checkout(request):
    ''' A view to return the checkout screen '''
    bag = request.session.get('bag', {})
    if bag == {}:
        return redirect(shopping_bag)

    return render(request, 'checkout/checkout.html', context)