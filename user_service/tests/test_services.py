from django.test import TestCase
from django.core.exceptions import ValidationError
from user_service.services import UserService

class UserServiceTests(TestCase):

    def test_register_user_success(self):
        # Test the successful registration of a user
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        
        user = UserService.register_user(**user_data)

        # Ensure the user is created
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('password123'))
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_register_user_fail(self):
        # Test that a validation error is raised if any fields are missing
        with self.assertRaises(ValidationError):
            UserService.register_user(username='', email='', password='', first_name='', last_name='')
