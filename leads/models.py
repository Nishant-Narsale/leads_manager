from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=100,unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name