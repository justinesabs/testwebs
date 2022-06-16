from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .cart import Cart

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'carts/menu_cart.html')

def cart(request):
    return render(request, 'carts/cart.html')

@login_required
def checkout(request):
    return render(request, 'carts/checkout.html')

def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')


