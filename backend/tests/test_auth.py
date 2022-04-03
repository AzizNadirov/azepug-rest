from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase

from apps.base.views import get_models

class TestAuth(APITestCase):
    def setUp(self):
        self.models = get_models()
        self.Profile = self.models['profile']

    def test_register(self):
        url = reverse('register')
        data = {'email' : "donfeyzulla@gm.com", 'user_name':'don', 'first_name':'Feyzulla','surname':'Feyzi',
                'password': 'testing123', 'about':'test_about'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        user = self.Profile.objects.get(user_name = 'don')
        self.assertEqual(user.user_name, 'don')
        self.assertEqual(user.first_name, 'Feyzulla')
        self.assertEqual(user.email, 'donfeyzulla@gm.com')
        self.assertEqual(user.surname, 'Feyzi')
        self.assertEqual(user.about, 'test_about')

    def test_obtain_tokens(self):
        reg_url = reverse('register')
        reg_data = {'email' : "donfeyzulla@gm.com", 'user_name':'don', 'first_name':'Feyzulla','surname':'Feyzi', 'password': 'testing123'}
        self.client.post(reg_url, reg_data)

        user = self.Profile.objects.get(user_name = 'don')
        token_url = reverse('token_obtain_pair')
        token_data = {'email' : "donfeyzulla@gm.com",'password': 'testing123'}
        response = self.client.post(token_url, token_data)
        self.assertIsNotNone(response.json().get('access', None))
        self.assertIsNotNone(response.json().get('refresh', None))

    def test_update_user(self):
        user = self.Profile.objects.create(
            user_name = 'feyzu',
            email = 'donfeyzulla@gm.com',
            first_name = 'Feyzulla',
            password = make_password('testing123')
        )
        # user.save()
        self.assertEqual(self.Profile.objects.count(), 1)
        self.assertEqual(user.user_name, 'feyzu')
        self.assertEqual(user.email, 'donfeyzulla@gm.com'),
        self.assertEqual(user.first_name, 'Feyzulla'),

        url = reverse('detail_user', kwargs={'user_name':'feyzu'})
        data = {'about': 'new about'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 403)

        token = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")
        response2 = self.client.patch(url, data)
        response3 = self.client.get(url)
        print(response3.data)
        self.assertEqual(response2.status_code, 200) # fails here: 403 != 200



