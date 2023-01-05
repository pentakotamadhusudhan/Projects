from django.test import TestCase
from rest_framework.reverse import reverse

from .seriliazers import loginseriliazer
from django.apps import apps
# Create your tests here.
class logintestcase(TestCase):
    def setUpClass(self):
        self.name='mobileapp'
        self.passowrd = '21313'

    def test_login(self):
        employe = apps.get_model('crud','employee')
        user = employe.objects.create_user('username', 'Pas$w0rd')
        self.client.login(username='mobileapp', password=self.passowrd)
        response = self.client.get(reverse('check_user'))
        self.assertEqual(response.status_code,200)