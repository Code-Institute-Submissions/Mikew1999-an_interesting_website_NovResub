''' Render '''
from django.shortcuts import render
from products.models import Category


def index(request):
    ''' Shows home page '''
    username = None
    user = request.user
    categories = Category.objects.all()

    if user.is_authenticated:
        username = request.user.username

    context = {
        'username': username,
        'categories': categories,
    }

    return render(request, 'home/index.html', context)
