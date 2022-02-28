from rest_framework import test
from rest_framework.test import APIClient
from django.test import Client
from django.urls import reverse
from django.contrib import auth
# from rest_framework.authtoken.models import Token
# from users import urls

User = auth.get_user_model()


class CheckAddingEmployeeTests(test.APITestCase):

    def setUp(self):
        Client.login(self, username="ctsadmin", password="ctsadmin")
        self.name = "alex"
        self.emp_id = 5
        self.company_id = 1
        self.department = "developer"
        self.gender = 1
        self.age = 24
        self.dob = "1998-01-01"
        self.salary = 20000

    def test_add_employee(self):
        client = APIClient()
        client.credentials(
            HTTP_AUTHORIZATION='Token 7d9e30c314a1d3bdf568df317a272141bb562766')
        response = self.client.post(
            reverse('employee'),
            data={
                'name': self.name,
                'emp_id': self.emp_id,
                'company_id': self.age,
                'department': self.department,
                'gender': self.gender,
                'age': self.age,
                'dob': self.dob,
                'salary': self.salary
            })
        self.assertEqual(response.status_code, 201)