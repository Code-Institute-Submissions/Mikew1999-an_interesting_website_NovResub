from django.shortcuts import render

# Create your views here.
def shopping_bag(request):
    ''' A view to return the shopping bag '''
    return render(request, 'shopping_bag/shopping_bag.html')