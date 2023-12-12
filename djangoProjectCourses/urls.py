"""
URL configuration for djangoProjectCourses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.auth import views
from django.urls import path, include
from django.contrib.auth import views as auth_views, views

from userextend.forms import AuthenticationNewForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("home.urls")),
    path('about/', include("about.urls")),
    path('course_detail/', include("course_detail.urls")),
    path('course/', include("courses.urls")),
    path('events/', include("events.urls")),
    path('pricing/', include("pricing.urls")),
    path('trainer/', include("trainer.urls")),
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),

    path('user/', include("userextend.urls")),
    path('student/', include("student.urls")),
    path('order/', include("order.urls")),
    path('cart/', include("cart.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
