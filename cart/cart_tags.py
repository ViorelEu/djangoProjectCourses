# cart_tags.py (inside your cart app)

from django import template
from cart.models import Cart

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        return cart.courses.count()
    return 0
