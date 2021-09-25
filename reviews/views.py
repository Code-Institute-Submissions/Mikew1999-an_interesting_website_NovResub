from django.shortcuts import render, redirect
from .forms import ReviewForm
from products.models import Products
from .models import Review
from django.contrib.auth.models import User


def review(request, product_id):
    ''' A view to return the reviews form '''
    form = ReviewForm()
    product = Products.objects.filter(pk=product_id)
    user = request.user
    username = None

    if user.is_authenticated:
        user_id = user.id
        username = user.username

    if username == None:
        return redirect('account_login')

    if request.POST:
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            review_description = form.cleaned_data['review_description']
            rating = form.cleaned_data['rating']
            user = User(user_id)
            product = Products(product_id)

            new_review = Review(product=product, user=user, rating=rating,
                                review_description=review_description, title=title)
            new_review.save()

            return redirect('products')

    context = {
        'form': form,
        'product': product,
        'product_id': product_id,
    }

    return render(request, 'reviews/product_review.html', context)
