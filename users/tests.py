from rest_framework import test
from django.urls import reverse
from django.contrib import auth
# from users import urls

User = auth.get_user_model()


class SignUpTest(test.APITestCase):

    def setUp(self):
        self.first_name = "test",
        self.username = "testuser",
        self.password = "testuser",
        self.mobile_number = "9898989898",
        self.country_code = "+91",
        self.email = "testuser@gmail.com",
        self.user_type = "staff"

    def test_signup(self):
        response = self.client.post(
            reverse('signup'),
            data={
                    'first_name': self.first_name,
                    'username': self.username,
                    'email': self.email,
                    'mobile_number': self.mobile_number,
                    'password': self.password,
                    'user_type': self.user_type,
                    'country_code': self.country_code})
        self.assertEqual(response.status_code, 201)
