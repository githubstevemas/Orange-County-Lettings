from django.test import TestCase
from django.urls import reverse


class LettingsViewsTests(TestCase):
    def test_letting_index_view(self):
        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertEqual(response.status_code, 200)
