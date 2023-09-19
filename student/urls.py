from django.urls import path

from student import views
from student.models import Student
from student.views import student

urlpatterns = [
    path('', student, name='student'),
    path('create_student/', views.StudentCreateView.as_view(), name="create-student"),
    path('list/', views.StudentListView.as_view(), name='list-of-students'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update-student'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete-student'),
    path('detail/<int:pk>/', views.StudentDetailView.as_view(), name="detail-student"),
    path('search/', views.search, name='search'),

]