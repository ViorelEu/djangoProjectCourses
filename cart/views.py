from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from courses.models import Course
from .models import ShoppingCart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Order
from cart.models import ShoppingCart

@login_required
def view_cart(request):
    try:
        cart = ShoppingCart.objects.get(user=request.user)
    except ShoppingCart.DoesNotExist:
        cart = ShoppingCart(user=request.user)
        cart.save()

    cart_items = cart.items.all()
    total_price = sum(item.price for item in cart_items)

    context = {
        'cart': {
            'items': cart_items,
            'total_price': total_price,
        }
    }

    return render(request, 'cart/view_cart.html', context)

@login_required
def add_to_cart(request, course_id):
    try:
        cart = ShoppingCart.objects.get(user=request.user)
    except ShoppingCart.DoesNotExist:
        cart = ShoppingCart(user=request.user)
        cart.save()

    course = Course.objects.get(id=course_id)
    cart.items.add(course)
    return redirect('view_cart')

@login_required
def remove_from_cart(request, course_id):
    cart = ShoppingCart.objects.get(user=request.user)
    course = Course.objects.get(id=course_id)
    cart.items.remove(course)
    return redirect('view_cart')


@login_required
def checkout_cart(request):
    try:
        cart = ShoppingCart.objects.get(user=request.user)
    except ShoppingCart.DoesNotExist:
        cart = ShoppingCart(user=request.user)
        cart.save()

    if request.method == 'POST':
        # Convert the shopping cart to an order
        order = cart.convert_to_order()
        return redirect('view_orders')

    cart_items = cart.items.all()
    total_price = sum(item.price for item in cart_items)

    context = {
        'cart': {
            'items': cart_items,
            'total_price': total_price,
        }
    }

    return render(request, 'cart/checkout_cart.html', context)

