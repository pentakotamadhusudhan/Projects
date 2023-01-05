from django.test import TestCase
from .models import employee
# Create your tests here.
class regtestcase(TestCase):
    def setUp(self):
        print('setup testcase')
        employee.objects.create(name='people',department='EEE',password='1245')
        employee.objects.create(name='people',department='EEE',password='1245')

    def test_employee(self):
        madhu=employee.objects.all()

        e2=employee.objects.get(name='people')
        print(madhu)
        self.assertEqual(madhu.count(),2)
        print('---------------madhu-------')
    def test_method(self):
        e1 = employee.objects.get(name='people')
        self.assertEqual(e1.get_name(),{'name':'people',
                  'department':'EEE',
                  'password':'1245'})
        self.assertEqual(e1.department,'EEE')

