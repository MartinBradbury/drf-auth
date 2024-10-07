from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserAuth(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return f"{self.email}'s account"
    
    
