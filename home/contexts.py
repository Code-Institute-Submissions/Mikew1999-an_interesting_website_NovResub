from products.models import Products
from reviews.models import Review


def mostPopular(request):
    ''' A view to check and return the most popular products '''
    products = Products.objects.all()
    product_list = []
    for product in products:
        if product.rate > 0:
            product_list.append(product)

    context = {
        'topProducts': product_list,
    }

    return context
