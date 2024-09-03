from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Model representing an address.

    Attributes:
        number (PositiveIntegerField): positive integer, max value 99999
        street (CharField): string, max 64 characters
        city (CharField): string, max 64 characters
        state (CharField): exactly 2 characters
        zip_code (PositiveIntegerField): positive integer, max value 99999
        country_iso_code (CharField): exactly 3 characters
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3,
                                        validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        String representation of the Address.

        Returns:
            str: The address in the format number+street.
        """

        return f'{self.number} {self.street}'

    class Meta:
        """
        Meta options for the Address model.
        """

        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Model representation of letting.

    Attributes:
        title (CharField): string, max 256 characters
        address (OneToOneField): one-to-one relationship with the Address model
            if the address is deleted, the letting will also be deleted.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the Letting.

        Returns:
            str: The title of the letting.
        """

        return self.title
