from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.models import User
from products.models import Products
from shopping_bag.contexts import bag_items
import stripe


def checkout(request):
    ''' A view to return the checkout screen '''
    bag = request.session.get('bag', {})
    user = request.user.id
    delivery = False

    if bag == {}:
        return redirect('shopping_bag')

    if request.POST:
        if 'address_line_1' in request.POST:
            address_line_1 = request.POST['address_line_1']
            if 'address_line_2' in request.POST:
                address_line_2 = request.POST['address_line_2']
            else:
                address_line_2 = ""
            town = request.POST['town']
            post_code = request.POST['post_code']
            email = request.POST['email']
            phone = request.POST['phone']

            delivery = {
                'address_line_1': address_line_1,
                'address_line_2': address_line_2,
                'town': town,
                'post_code': post_code,
                'email': email,
                'phone': phone,
                'user': user
            }

            request.session['delivery'] = delivery
            return redirect(order_summary)

    context = {
        'user': user,
        'delivery_details': delivery,
    }

    return render(request, 'checkout/checkout.html', context)


def order_summary(request):
    ''' A view to return the order summary page '''
    delivery = request.session.get('delivery', {})
    return render(request, 'checkout/order_summary.html', delivery)


def bank_details(request):
    ''' A view to return billing details form '''
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})

    if bag == {}:
        return redirect('shopping_bag')

    current_bag = bag_items(request)
    total = current_bag['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )

    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    
    return render(request, 'checkout/bank_details.html', context)


def success(request):
    ''' '''
    return render(request, 'checkout/success.html')


def cancel(request):
    ''' '''
    return render(request, 'checkout/cancel.html')
