from django.urls import reverse
from . import models
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date


class ProjectTestCase(APITestCase):
    """
    Test cases for project app
    """

    def setUp(self):
        self.project = models.Project.objects.create(title="Zender",
                                                     description="A file transfer application",
                                                     created=date.today(),
                                                     thumbnail="sample-file.png",
                                                     domain="ds",
                                                     )

    def test_project_list(self):
        response = self.client.get(reverse("project:list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Project.objects.all().count(), 1)
        self.assertEqual(models.Project.objects.get().title, "Zender")

    def test_project_detail(self):
        response = self.client.get(
            reverse("project:detail", args=(self.project.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_create(self):
        data = {
            "title": "Zender - Updated",
            "description": "A file transfer application",
            "created": date.today(),
            "title": "Zender - Updated",
            "domain": "ds",
            "thumbnail": "wrong.png",
        }

        response = self.client.put(reverse("project:list"), data)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_project_delete(self):
        response = self.client.delete(
            reverse("project:detail", args=(self.project.id,)))
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_project_update(self):
        data = {
            "title": "Zender - Updated",
            "description": "A file transfer application",
            "created": date.today(),
            "title": "Zender - Updated",
            "domain": "ds",
        }

        response = self.client.put(
            reverse("project:detail", args=(self.project.id,)), data)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(
            reverse("project:detail", args=(self.project.id,)), data)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
