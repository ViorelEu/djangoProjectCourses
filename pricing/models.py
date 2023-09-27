from django.db import models


# Subsctiption model care contine title, price, description
class Subscription(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.price}"


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    # Your existing Course model fields

    # Add a ManyToManyField to connect courses with subscriptions
    subscriptions = models.ManyToManyField(Subscription, blank=True)
    title = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title
