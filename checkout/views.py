''' Checkout pages and form handling '''
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
import stripe
from shopping_bag.contexts import bag_items
from .models import DeliveryDetails
from .forms import Delivery


def checkout(request):
    ''' A view to return the checkout screen '''
    bag = request.session.get('bag', {})
    user = request.user.id

    if bag == {}:
        return redirect('shopping_bag')

    context = {
        'user': user,
    }

    return render(request, 'checkout/checkout.html', context)


def address(request):
    ''' A view to return the delivery details page '''
    address_details = request.session.get('address_details', {})
    form = Delivery()
    if request.POST:
        address_line_1 = request.POST['address_line_1']
        if 'address_line_2' in request.POST:
            address_line_2 = request.POST['address_line_2']
        else:
            address_line_2 = ''
        town = request.POST['town']
        postcode = request.POST['postcode']
        email = request.POST['email']
        phone = request.POST['phone']

        if 'guest' in request.POST:
            address_details['1'] = {
                'address_line_1': address_line_1,
                'address_line_2': address_line_2,
                'town': town,
                'postcode': postcode,
                'email': email,
                'phone': phone
            }

        else:
            new_delivery_details = DeliveryDetails(
                user=User(request.user.id),
                address_line_1=address_line_1, address_line_2=address_line_2,
                town=town, postcode=postcode, email=email, phone=phone
            )
            new_delivery_details.save()

        request.session['address_details'] = address_details

        return redirect('order_summary')

    context = {
        'form': form,
    }

    return render(request, 'checkout/delivery_details.html', context)


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
    ''' Order Success page '''
    return render(request, 'checkout/success.html')


def cancel(request):
    ''' Cancels transaction '''
    return render(request, 'checkout/cancel.html')
