from django.shortcuts import render
from .forms import ReviewForm
from products.models import Products


def review(request, product_id):
    ''' A view to return the reviews form '''
    form = ReviewForm()
    product = Products.objects.filter(pk=product_id)

    context = {
        'form': form,
        'product': product,
        'product_id': product_id,
    }

    return render(request, 'reviews/product_review.html', context)