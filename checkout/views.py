from django.shortcuts import render, redirect


def checkout(request):
    ''' A view to return the checkout screen '''
    bag = request.session.get('bag', {})
    user = request.user

    if bag == {}:
        return redirect(shopping_bag)

    context = {
        'user': user,
    }

    return render(request, 'checkout/checkout.html', context)