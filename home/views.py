from django.shortcuts import render


def index(request):
    ''' Shows home page '''
    username = None
    user = request.user
 
    if user.is_authenticated:
        username = request.user.username

    context = {
        'username': username,
    }

    return render(request, 'home/index.html', context)
