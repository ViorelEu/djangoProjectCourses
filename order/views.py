from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Order
from cart.models import ShoppingCart

@login_required
def view_orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders,
    }
    return render(request, 'order/view_orders.html', context)
