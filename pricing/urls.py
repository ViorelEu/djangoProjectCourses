from django.urls import path

from .views import pricing

urlpatterns = [
    path('pricing/', pricing, name='pricing')
]