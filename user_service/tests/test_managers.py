from django.test import TestCase
from user_service.models import User

class UserManagerTests(TestCase):

    def test_create_user(self):
        # Create a normal user using the custom manager
        user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="password123"
        )
        
        # Test user properties
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("password123"))  # Ensure password is hashed
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)



    def test_create_superuser(self):
        # Create a superuser using the custom manager
        superuser = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="admin123"
        )
        
        # Test superuser properties
        self.assertEqual(superuser.username, "admin")
        self.assertEqual(superuser.email, "admin@example.com")
        self.assertTrue(superuser.check_password("admin123"))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_user_without_email(self):
        # Test creating a user without email should raise ValueError
        with self.assertRaises(ValueError):
            User.objects.create_user(username="testuser", email="", password="password123")
