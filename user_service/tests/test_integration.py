from django.test import TestCase
from django.urls import reverse
from user_service.models import User

class RegisterIntegrationTest(TestCase):
    def setUp(self):
        """
        Set up initial data for testing.
        """
        self.register_url = reverse('user_service:register') # Ensure this matches your URL name
        self.valid_user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "securepassword123",
            "first_name": "Test",
            "last_name": "User",
        }

    def test_register_user_success(self):
        """
        Test that a user can be registered successfully.
        """
        # Send POST request to the register API
        response = self.client.post(self.register_url, data=self.valid_user_data)

        # Assert the API returns a 201 Created status
        self.assertEqual(response.status_code, 201)

        # Assert the user exists in the database
        self.assertTrue(User.objects.filter(username="testuser").exists())

        # Verify the user data in the database
        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, self.valid_user_data["email"])
        self.assertEqual(user.first_name, self.valid_user_data["first_name"])

    def test_register_user_failure(self):
        """
        Test that registration fails with invalid data.
        """
        # Send POST request with missing fields
        invalid_user_data = {
            "username": "",
            "email": "invalidemail",
            "password": "123",  # Weak password
        }
        response = self.client.post(self.register_url, data=invalid_user_data)

        # Assert the API returns a 400 Bad Request status
        self.assertEqual(response.status_code, 400)

        # Assert no user is created
        self.assertEqual(User.objects.count(), 0)
