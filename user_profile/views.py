from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def user_profile(request, user_id):
    ''' A view to return the users profile '''
    user = get_object_or_404(User, id=user_id)

    context = {
        'user': user,
    }

    return render(request, 'user_profile/user_profile.html', context)
