from json import dumps

from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from reminder.models import MyUser


class RestTest(APITestCase):
    def setUp(self):
        self.login = "test_name"
        self.pwd = "test_pwd"
        self.user = MyUser.objects.create_user(
            username=self.login,
            password=self.pwd
        )

    def test_create_token(self):
        url = reverse("create-token")
        data = {
            "login": self.login,
            "pwd": self.pwd
        }
        response = self.client.post(
            path=url,
            data=dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Token.objects.get(user=self.user).__str__(),
            response.json()['token']
        )
