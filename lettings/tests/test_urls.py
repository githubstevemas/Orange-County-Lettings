from django.test import TestCase
from django.urls import reverse


class LettingsUrlTests(TestCase):
    """
    Tests for the urls of profiles application.
    """

    def test_wrong_letting_url(self):
        """
        Ensures that a wrong letting returns 404 status code.
        Ensures the 404.html template is used.
        """

        response = self.client.get(
            reverse("lettings:letting", args=[666])
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
