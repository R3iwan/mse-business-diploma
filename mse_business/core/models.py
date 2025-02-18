from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    status = models.TextField(max_length=10)
    
    def __str__(self):
        return f'{self.first_name}'