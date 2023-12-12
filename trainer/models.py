from django.db import models

# Create your models here.
class Trainer(models.Model):

    departament_options=(
        ("Backend", 'backend'),
        ("Frontend", 'frontend'),
        ("Network", 'network')

    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    department = models.CharField(max_length=8, choices=departament_options, null=True)
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='profile/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Pip install pillow -> este folosit pentru a manipula imaginile.

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
