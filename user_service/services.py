from .models import User
from django.core.exceptions import ValidationError

class UserService:
    @staticmethod
    def register_user(username, email, password, first_name, last_name):
        """
        This method handles the user registration process.
        """
        try:
            # Create the user via the custom manager
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            return f'{user.username} user was created'
        except Exception as e:
            # Handle any exceptions and raise a validation error if needed
            raise ValidationError(f"Error registering user: {str(e)}")
