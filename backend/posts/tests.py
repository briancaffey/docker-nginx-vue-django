"""
Unit Tests for Post Models
"""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from rest_framework_jwt.settings import api_settings


# Create your tests here.

class TestPosts(TestCase):
    """Post Tests"""

    def test_get_posts(self):
        """Unauthenticated users can access posts APIListView"""
        url = reverse('posts')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK) #status.HTTP_400_BAD_REQUEST)

    def test_header_for_token_verification(self):
        """
        https://stackoverflow.com/questions/47576635/django-rest-framework-jwt-unit-test
        """
        url = reverse('posts')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK) #status.HTTP_200_OK)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user = User.objects.create_user(username='user', email='user@foo.com', password='pass')
        user.is_active = True
        user.save()
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)


        verify_url = reverse('jwt-verify')
        credentials = {
            'token': token
        }

        print("creds: ", credentials)
        resp = self.client.post(verify_url, credentials, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
