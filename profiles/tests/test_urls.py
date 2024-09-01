from django.test import TestCase
from django.urls import reverse


class ProfilesUrlTests(TestCase):
    def test_wrong_profile_url(self):

        response = self.client.get(
            reverse('profiles:profile', args=[666])
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
