from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('shopping_bag/', include('shopping_bag.urls')),
    path('reviews/', include('reviews.urls')),
    path('checkout/', include('checkout.urls')),
    path('user_profile/', include('user_profile.urls')),
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
