from django.db import models

# Create your models here.
class History(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=500)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.message
