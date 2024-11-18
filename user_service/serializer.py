from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # The password will be write-only

    class Meta:
        model = User  # Reference to the custom User model
        fields = ['username', 'email', 'password', 'first_name', 'last_name']  # Fields to be included in registration

    def create(self, validated_data):
        # Create a user with a hashed password (use `create_user` method provided by AbstractUser)
        user = User.objects.create_user(**validated_data)
        return user

