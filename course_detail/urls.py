from django.urls import path

from .views import course_detail

urlpatterns = [
    path('', course_detail, name='course-detail')
]