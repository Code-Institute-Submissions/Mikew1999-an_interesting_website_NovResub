from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from products.models import Products


def user_profile(request, user_id):
    ''' A view to return the users profile '''
    user = get_object_or_404(User, id=user_id)
    product_count = Products.objects.filter(author=User(user_id)).count()
    products = None
    products = Products.objects.filter(author=User(user_id))[:4]
    orders = None

    context = {
        'user': user,
        'products': products,
        'product_count': product_count,
        'orders': orders,
    }

    return render(request, 'user_profile/user_profile.html', context)
