from products.models import Products
from reviews.models import Review


def CalculateRating(product_id):
    reviews = Review.objects.all()
    products = []
    for review in reviews:
        products.append(review.product.pk)

    if product_id in products:
        product = Products.objects.filter(pk=product_id)
        number_of_reviews = product.count()
        ratings = 0
        # product.count = number_of_reviews
        reviews = reviews.filter(product=Products(product_id))
        for review in reviews:
            ratings += review.rating

        for x in product:
            x.count = reviews.count()
            x.rate = ratings / reviews.count()
            x.save()

    return products
