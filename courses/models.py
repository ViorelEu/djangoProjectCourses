# models.py

from django.db import models
from django.contrib.auth.models import User
from pricing.models import Subscription
# added comment
# add new row
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Rating(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s rating for {self.course.title}"

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=50)
    start_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ImageField(upload_to='profile/', null=True)
    duration_in_weeks = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    subscriptions = models.ManyToManyField(Subscription, related_name='courses')
    purchases = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    outline = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='courses', blank=True)

    def __str__(self):
        return self.title
