from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import CustomUser


class UserProfileAPITests(APITestCase):

    def test_authenticated_user_can_get_profile(self):
        user = CustomUser(
            id=1,
            username='testuser',
            email='test@example.com',
            first_name='Test',
            last_name='User',
        )
        client = APIClient()
        client.force_authenticate(user=user)

        response = client.get('/api/accounts/profile/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
        })

    def test_unauthenticated_user_cannot_get_profile(self):
        response = self.client.get('/api/accounts/profile/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
