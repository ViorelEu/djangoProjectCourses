from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from order.models import Order


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Course, related_name='carts', blank=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def convert_to_order(self):
        cart_items = self.items.all()
        total_price = sum(item.price for item in cart_items)

        order = Order.objects.create(
            user=self.user,
            total_price=total_price,
        )
        order.courses.set(cart_items.all())
        order.save()
        self.items.clear()
        return order
