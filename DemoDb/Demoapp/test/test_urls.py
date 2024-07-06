from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Demoapp.views import home,addEmployee

class TestUrl(SimpleTestCase):

    def test_home(self):
        url=reverse('home')
        self.assertEqual(resolve(url).func,home)

    def test_addEmployee(self):
        url=reverse('add')
        self.assertEqual(resolve(url).func,addEmployee)