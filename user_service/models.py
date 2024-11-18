from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        Group,
        related_name='user_set_custom',  # Change this to avoid the conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions_custom',  # Change this to avoid the conflict
        blank=True
    )
