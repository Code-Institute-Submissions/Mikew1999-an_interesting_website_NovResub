''' Checkout pages and form handling '''
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
import stripe
from shopping_bag.contexts import bag_items
from .models import Order


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
    bag = request.session.get('bag', {})

    if bag == {}:
        return redirect('shopping_bag')

    address_details = request.session.get('address_details', {})
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

        address_details['1'] = {
            'address_line_1': address_line_1,
            'address_line_2': address_line_2,
            'town': town,
            'postcode': postcode,
            'email': email,
            'phone': phone
        }

        request.session['address_details'] = address_details

        return redirect('order_summary')

    context = {
        'address_details': address_details,
    }

    return render(request, 'checkout/delivery_details.html', context)


def order_summary(request):
    ''' A view to return the order summary page '''
    address_details = request.session.get('address_details', {})
    bag = bag_items(request)
    print(bag['items'])
    context = {
        'address_details': address_details,
    }

    return render(request, 'checkout/order_summary.html', context)


def create_checkout_session(request):
    bag = bag_items(request)
    delivery_cost = request.session.get('delivery_cost', {})
    unit_amount = round(bag['total'], 2) + round(delivery_cost['cost'], 2)
    unit_amount = round(unit_amount * 100)
    print(unit_amount)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': 'T-shirt',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://an-interesting-website.herokuapp.com/checkout/success',
        cancel_url='https://an-interesting-website.herokuapp.com/checkout/cancel')

    return redirect(session.url, code=303)


def success(request):
    ''' Order Success page '''
    print(request.META.get('HTTP_REFERER'))
    new_delivery_details = DeliveryDetails(
        user=User(request.user.id),
        address_line_1=address_line_1, address_line_2=address_line_2,
        town=town, postcode=postcode, email=email, phone=phone
    )
    new_delivery_details.save()
    return render(request, 'checkout/success.html')


def cancel(request):
    ''' Cancels transaction '''
    return render(request, 'checkout/cancel.html')
