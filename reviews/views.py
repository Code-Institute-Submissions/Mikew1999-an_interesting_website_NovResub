from django.shortcuts import render


def review(request):
    ''' A view to return the reviews form '''
    
    return render(request, 'reviews/product_review.html')