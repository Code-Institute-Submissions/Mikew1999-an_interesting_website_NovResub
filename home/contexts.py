from products.models import Products
from reviews.models import Review


def mostPopular(request):
    ''' A view to check and return the most popular products '''
    products = Products.objects.all()

    products = products.order_by('rate')[:4]
    context = {
        'topProducts': products,
    }

    return context
