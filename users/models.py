from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    reset_password_token = models.CharField(max_length=64, blank=True, null=True)

    ADMIN = 'admin'
    CLIENT = 'client'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (CLIENT, 'Client'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CLIENT)
    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email  
        super().save(*args, **kwargs)
