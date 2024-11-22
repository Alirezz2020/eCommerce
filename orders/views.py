from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from home.models import Product
from .cart import Cart
from .forms import CartAddForm


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {"cart": cart})

class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
            messages.success(request, 'Your cart has been updated')
        return redirect('orders:cart')



class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        messages.success(request, 'Your cart has been removed')
        return redirect('orders:cart')
