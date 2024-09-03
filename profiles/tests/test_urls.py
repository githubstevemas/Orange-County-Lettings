from django.test import TestCase
from django.urls import reverse


class ProfilesUrlTests(TestCase):
    """
    Tests for the urls of profiles application.
    """

    def test_wrong_profile_url(self):
        """
        Ensures that a wrong profile returns 404 status code.
        Ensures the 404.html template is used.
        """

        response = self.client.get(
            reverse('profiles:profile', args=[666])
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
