from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingsViewsTests(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number="742",
            street="Evergreen Terrace",
            city="Springfield",
            state="IL",
            zip_code="80085",
            country_iso_code="USA"
        )

        self.letting = Letting.objects.create(
            title="Charming Cottage",
            address=self.address
        )

    def test_letting_index_view(self):
        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertEqual(response.status_code, 200)

    def test_letting_view(self):
        response = self.client.get(reverse('lettings:letting',
                                           args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Charming Cottage")

