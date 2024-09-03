from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingsViewsTests(TestCase):
    """
    Tests for the views of lettings application.
    """

    def setUp(self):
        """
        Set up the test environment by creating a test address and letting.
        This method is called before every test method to prepare the objects
        required for testing.
        """

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
        """
        Test the lettings index view.

        Ensures that the lettings index page loads successfully and
        returns 200 status code.
        """

        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertEqual(response.status_code, 200)

    def test_letting_view(self):
        """
        Test the individual letting view.

        Ensures that a specific letting page loads successfully and
        returns 200 status code.
        Contains the title of the letting.
        """

        response = self.client.get(reverse('lettings:letting',
                                           args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Charming Cottage")
