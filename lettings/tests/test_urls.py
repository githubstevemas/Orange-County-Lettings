from django.test import TestCase
from django.urls import reverse


class LettingsUrlTests(TestCase):
    def test_wrong_letting_url(self):

        response = self.client.get(
            reverse("lettings:letting", args=[666])
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
