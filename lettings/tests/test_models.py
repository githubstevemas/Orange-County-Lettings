from django.test import TestCase
from lettings.models import Address, Letting


class TestLettingsModels(TestCase):

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

    def test_letting_creation(self):
        assert self.letting.title == "Charming Cottage"
        assert self.address.street == "Evergreen Terrace"

    def test_letting_str(self):
        assert str(self.letting) == "Charming Cottage"
