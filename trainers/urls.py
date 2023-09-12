from django.urls import path

from .views import trainer

urlpatterns = [
    path('trainer/', trainer, name='trainer')
]