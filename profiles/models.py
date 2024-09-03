from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Model representation of profile.

    Attributes:
        user (OneToOneField): one-to-one relationship with the User model
            if the user is deleted, the profile will also be deleted
        favorite_city (CharField): string, max 64 characters. Can be empty
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        String representation of the Profile.

        Returns:
            str: The username of the profile user.
        """
        return self.user.username
