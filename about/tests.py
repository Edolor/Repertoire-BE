from urllib import response
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class AboutTestCase(APITestCase):
    def test_about_list(self):
        response = self.client.get(reverse("about:list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_about_unauth_methods(self):
        data = {}
        response = self.client.post(reverse("about:list"), data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(reverse("about:list"), data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(reverse("about:list"), data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(reverse("about:list"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)