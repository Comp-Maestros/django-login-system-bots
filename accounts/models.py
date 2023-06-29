from django.db import models
#want to use AbstractUser
from django.contrib.auth.models import AbstractUser

# Create your models here. and use email field to login

class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    def __str__(self):
        return self.email
    
