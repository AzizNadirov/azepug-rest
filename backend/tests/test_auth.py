import email
from django.utils import timezone
from django.urls import reverse

from rest_framework.test import APITestCase

from apps.base.views import get_models

class TestAuth(APITestCase):
    def setUp(self):
        self.models = get_models()

    def test_register(self):
        url = reverse('register')
        data = {'email' : "donfeyzulla@gm.com", 'user_name':'don', 'first_name':'Feyzulla','surname':'Feyzi', 'password': 'testing123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        user = self.models['profile'].objects.get(user_name = 'don')
        self.assertEqual(user.user_name, 'don')
        self.assertEqual(user.first_name, 'Feyzulla')
        self.assertEqual(user.email, 'donfeyzulla@gm.com')
        self.assertEqual(user.surname, 'Feyzi')

