from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import AddressDetails


def checkout(request):
    ''' A view to return the checkout screen '''
    bag = request.session.get('bag', {})
    user = request.user
    delivery_details = False
    delivery_cost = None
    form = AddressDetails()

    if bag == {}:
        return redirect('shopping_bag')

    if request.POST:
        form = AddressDetails(request.POST)
        if form.is_valid():
            address_line_1 = form.cleaned_data['address_line_1']
            address_line_2 = form.cleaned_data['address_line_2']
            town = form.cleaned_data['town']
            post_code = form.cleaned_data['post_code']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            if user.is_authenticated:
                user_id = user.id
                new_delivery_details = AddressDetails(
                    address_line_1=address_line_1, address_line_2=address_line_2, town=town, post_code=post_code, phone=phone, user=User(user_id))
                new_delivery_details.save()

                delivery_details = AddressDetails.objects.filter(
                    user=User(user_id))

            else:
                delivery_details = {
                    'address_line_1': address_line_1,
                    'address_line_2': address_line_2,
                    'town': town,
                    'post_code': post_code,
                    'email': email,
                    'phone': phone
                }

    context = {
        'user': user,
        'form': form,
        'user_id'
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
