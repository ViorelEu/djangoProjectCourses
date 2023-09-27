from django.urls import path

from .views import course_details

urlpatterns = [
    path('', course_details, name='course-details')
]