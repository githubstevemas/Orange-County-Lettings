import pytest

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_letting_creation():
    address = Address.objects.create(
        number="742",
        street="Evergreen Terrace",
        city="Springfield",
        state="USA",
        zip_code="80085",
        country_iso_code="SO 3166-2:US"
    )
    letting = Letting.objects.create(
        title="Charming Cottage",
        address=address
    )

    assert letting.title == "Charming Cottage"
    assert letting.address.street == "Evergreen Terrace"


@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number="742",
        street="Evergreen Terrace",
        city="Springfield",
        state="USA",
        zip_code="80085",
        country_iso_code="SO 3166-2:US"
    )
    letting = Letting.objects.create(
        title="Charming Cottage",
        address=address
    )

    assert str(letting) == "Charming Cottage"
