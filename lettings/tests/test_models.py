from django.test import TestCase
from lettings.models import Address, Letting


class TestLettingsModels(TestCase):
    """
    Tests models of lettings application.
    """

    def setUp(self):
        """
        Set up the test environment by creating an address and letting.
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

    def test_letting_creation(self):
        """
        Test the letting creation.

        Ensures that letting object is successfully created and
        his title and address are corrects.
        """
        assert self.letting.title == "Charming Cottage"
        assert self.address.street == "Evergreen Terrace"

    def test_letting_str(self):
        """
        Test the string representation.

        Ensures that the __str__ method returns the correct title.
        """
        assert str(self.letting) == "Charming Cottage"
