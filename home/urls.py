from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact_us', views.contact, name='contact_us'),
    path('about_us', views.about_us, name='about_us'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy')
]
