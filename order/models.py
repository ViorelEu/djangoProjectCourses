from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from courses.models import Course

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name='orders')
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    order_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
