''' Imports Products '''
from products.models import Products


def top_products(request):
    ''' A view to check and return the most popular products '''
    products = Products.objects.all().order_by('rate')[:4]

    context = {
        'top_products': products,
    }

    return context


def active_user(request):
    ''' Sets username variable '''
    username = None
    user = request.user
    if user.is_authenticated:
        username = request.user.username

    context = {
        'username': username,
    }

    return context
