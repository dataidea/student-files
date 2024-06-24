from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import ToDo, MemberLogin, MemberRegistration

# Create your tests here.

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Optionally, create some initial data for testing
        self.todo = ToDo.objects.create(activity='Test Activity')
        self.login = MemberLogin.objects.create(username='testuser', password='testpassword', email='test@example.com')
        self.registration_data = {
            'firstName': 'Salimu',
            'lastName': 'Kabogere',
            'email': 'salimu.kabogere@gmail.com',
            'password': 'password123',
            'comfirm_password': 'password123'
        }

    def test_todo_list(self):
        # Test retrieving list of todos
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login(self):
        # Test login endpoint
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@gmail.com'
        }
        response = self.client.post('/api/member-logins/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration(self):
        # Test registration endpoint
        response = self.client.post('/api/member-registrations/register/', self.registration_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
