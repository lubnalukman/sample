from django.test import TestCase
from Demoapp.models import Employee

class TestModel(TestCase):
    def testModelEmployee(self):
        emp=Employee.objects.create(name='zzz')
        print(emp)
        self.assertIsInstance(emp,Employee)