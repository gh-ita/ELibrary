from django.test import TestCase
from user_service.serializer import RegisterSerializer

class RegisterSerializerTests(TestCase):

    def test_valid_data(self):
        # Define valid data for user registration
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123", 
            "first_name":"ghita", 
            "last_name":"hatimi"
        }

        # Initialize the serializer with the valid data
        serializer = RegisterSerializer(data=data)
        
        # Check if the serializer is valid
        self.assertTrue(serializer.is_valid())

        # Check if the serializer creates the user correctly
        user = serializer.save()
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("password123"))  # Ensure the password is hashed

    def test_missing_fields(self):
        # Test missing required fields (e.g., email)
        data = {
            "username": "testuser",
            "password": "password123"
        }

        serializer = RegisterSerializer(data=data)

        # Check that the serializer is not valid due to missing fields
        self.assertFalse(serializer.is_valid())

        # Ensure the error is on the email field
        self.assertIn("email", serializer.errors)

    def test_invalid_email(self):
        # Test with an invalid email format
        data = {
            "username": "testuser",
            "email": "invalidemail",
            "password": "password123", 
            "first_name":"ghita", 
            "last_name":"hatimi"
        }

        serializer = RegisterSerializer(data=data)

        # Check that the serializer is not valid due to invalid email
        self.assertFalse(serializer.is_valid())

        # Ensure the error is on the email field
        self.assertIn("email", serializer.errors)

    def test_password_mismatch(self):
        # Test password mismatch (e.g., weak password)
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "123",  # This password is too weak
            "first_name": "ghita",
            "last_name": "hatimi",
        }

        # Create an instance of the serializer with the data
        serializer = RegisterSerializer(data=data)

        # Check that the serializer is not valid due to weak password
        self.assertFalse(serializer.is_valid())

        # Ensure the error is on the password field
        self.assertIn("password", serializer.errors)
