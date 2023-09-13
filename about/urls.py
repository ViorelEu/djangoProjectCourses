from django.urls import path

from .views import about, edit_about

urlpatterns = [
    path('about/', about, name='about'),
    path('edit_about/', edit_about, name='edit-about'),
]