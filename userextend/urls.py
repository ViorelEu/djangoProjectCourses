from django.urls import path

from userextend import views
from userextend.views import custom_logout

urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('logout/', custom_logout, name='logout')
]