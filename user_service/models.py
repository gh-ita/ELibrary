from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .managers import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)  # Email should be unique for each user
    first_name = models.CharField(max_length=100)  # Optional: You can add a first name
    last_name = models.CharField(max_length=100)   # Optional: You can add a last name
    is_admin = models.BooleanField(default=False)  # Custom field to check if the user is an admin
    objects = CustomUserManager()
    # Many-to-many fields to avoid conflicts with the default User model in Django
    groups = models.ManyToManyField(
        Group,
        related_name='user_set_custom',  # Custom reverse accessor name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions_custom',  # Custom reverse accessor name to avoid conflict
        blank=True
    )

    def __str__(self):
        return self.username  # Return the username when the user object is printed
    
    
    
    
    
    
    
