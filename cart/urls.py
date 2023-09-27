from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_cart, name='view_cart'),
    path('add/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:course_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_cart, name='checkout'),

]
