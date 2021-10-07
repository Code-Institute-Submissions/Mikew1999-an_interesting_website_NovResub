from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from products.models import Products
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
    stripe.api_key = 'sk_test_51Je9YQK25WcuIKuVMssctpYOXdCkUjS8SjLTzag9JiAPdHHWCtK870aIr4qNUZ4jd2NoCfCkJM16sfjiUacbyM4G00fDnjPJyh'
    line_items = []
    bag = request.session.get('bag', {})
    if bag == {}:
        return redirect('shopping_bag')

    for product_id, product_data in bag.items():
        product = get_object_or_404(Products, pk=product_id)
        # If item doesn't have size
        if isinstance(product_data, int):
            product_price = float(product.price)
            quantity = product_data

            line_items.append({
                'price': product_price,
                'quantity': quantity
            })
        else:
            product = get_object_or_404(Products, pk=product_id)
            # If item has size
            for size, quantity in product_data['items_by_size'].items():
                product_price = float(product.price)
                quantity = quantity
                line_items.append({
                    'price': product_price,
                    'quantity': quantity
                })

    delivery = request.session['delivery']
    email = delivery['email']

    if request.POST:
        my_domain = 'https://an-interesting-website.herokuapp.com/'
        try:
            checkout_session = stripe.checkout.Session.create(
                customer_email=email,
                submit_type='pay',
                billing_address_collection='auto',
                shipping_address_collection={
                    'allowed_countries': ['UK'],
                },
                line_items=line_items,
                payment_method_types=[
                    'card',
                    'bacs_debit',
                ],
                mode='payment',
                success_url=my_domain + 'checkout/success',
                cancel_url=my_domain + 'chekout/cancel',
            )
        except Exception as e:
            return str(e)

        return redirect('checkout_session.url', code=303)
    else:
        return redirect('shopping_bag')


def success(request):
    ''' '''
    return render(request, 'checkout/success.html')


def cancel(request):
    ''' '''
    return render(request, 'checkout/cancel.html')
