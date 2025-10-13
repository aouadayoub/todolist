from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email
