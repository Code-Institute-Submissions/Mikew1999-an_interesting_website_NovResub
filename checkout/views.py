from django.shortcuts import render, redirect
from django.contrib.auth.models import User


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
    bag = request.session.get('bag', {})
    if bag == {}:
        return redirect('shopping_bag')
    return render(request, 'checkout/bank_details.html')
