''' To check date '''
import datetime


def check_deals(request):
    ''' Applies deals to shopping bag '''
    day_of_week = datetime.datetime.now().isoweekday()

    if day_of_week in [1, 4]:
        current_deal = "Free Delivery on all orders"
    elif day_of_week in [5, 6]:
        current_deal = "10% off Electronics"
    else:
        current_deal = "10% off all items"

    return current_deal
