from django.urls import path

from .views import pricing, associate_subscription

# urlpatterns = [
#     path('', pricing, name='pricing')
# ]

from django.urls import path

from . import views
from .views import pricing

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pricing, name='pricing'),
    path('associate_subscription/<int:course_id>/', views.associate_subscription, name='associate_subscription'),
]
