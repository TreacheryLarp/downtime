from django.test import TestCase, Client

from players.models import *


class LoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='erik',
                                             email='erik@mail',
                                             password='erik')
        self.client = Client()

    def testLogin(self):
        response = self.client.get('/login/')
        self.assertContains(response, 'login')

        response = self.client.post('/login/',
                                    {'username': self.user.username,
                                     'password': self.user.password})
        self.assertContains(response, 'login')
