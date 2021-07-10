from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Matriculations-list")
        self.user = User.objects.create_user("c3po", password="123456")

    def test_authentication_user_credentials(self):
        """It should authentication a user when credentials right"""
        user = authenticate(username="c3po", password="123456")
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_request_get_authorized(self):
        """It should the GET request with user credentials"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
