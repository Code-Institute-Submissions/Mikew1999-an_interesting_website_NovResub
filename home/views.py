from django.shortcuts import render
from products.models import Category, Products


def index(request):
    ''' Shows home page '''
    username = None
    user = request.user
    categories = Category.objects.all()

    if user.is_authenticated:
        username = request.user.username

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            print(category)

    context = {
        'username': username,
        'categories': categories,
    }

    return render(request, 'home/index.html', context)
