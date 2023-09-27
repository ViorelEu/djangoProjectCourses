from django.db import models

from pricing.models import Subscription


# from pricing.models import Subscription


# Create your models here.





class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=50)
    start_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    duration_in_weeks = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Define the many-to-many relationship with Subscription
    subscriptions = models.ManyToManyField(Subscription, related_name='courses')

    def __str__(self):
        return self.title



