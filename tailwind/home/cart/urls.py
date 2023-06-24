from cart.views import add_to_cart, cart, checkout
from django.urls import path


urlpatterns = [
    path('add_to_cart/<int:product_id>', add_to_cart, name = 'add_to_cart'),
    path('', cart, name = 'cart'),
    path('checkout/', checkout, name = 'checkout'),
]
