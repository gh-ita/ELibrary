from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class RegisterViewTests(APITestCase):

    def test_register_user_success(self):
        # Define the registration data
        url = reverse('user_service:register')
        # Adjust the URL name if necessary
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe"
        }

        # Send POST request to the register view
        response = self.client.post(url, data, format='json')

        # Check the response status and message
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "User created successfully!")

    def test_register_user_failure(self):
        # Define invalid registration data
        url = reverse('user_service:register')
        data = {
            "username": "",
            "email": "invalidemail",
            "password": "",
            "first_name": "",
            "last_name": ""
        }

        # Send POST request with invalid data
        response = self.client.post(url, data, format='json')

        # Check that the response contains error messages
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)
        self.assertIn("email", response.data)
        self.assertIn("password", response.data)
 