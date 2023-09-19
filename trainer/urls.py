from django.urls import path

from trainer import views
from trainer.views import trainer

urlpatterns = [
    path('', trainer, name='trainer' ),
    path('create/', views.TrainerCreateView.as_view(), name="create-trainer"),
    path('list/', views.TrainerListView.as_view(), name='list-of-trainers'),
    path('update/<int:pk>/', views.TrainerUpdateView.as_view(), name='update-trainer'),
    path('delete/<int:pk>/', views.TrainerDeleteView.as_view(), name='delete-trainer'),
    path('detail/<int:pk>/', views.TrainerDetailView.as_view(), name='detail-trainer'),
]