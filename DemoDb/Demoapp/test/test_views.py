from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from Demoapp.models import Employee

class TestViews(TestCase):
    def setUp(self):
        # You can create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def testviewshome(self):
        client = Client()        
        # Authenticate the client
        client.login(username='testuser', password='testpass')
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')