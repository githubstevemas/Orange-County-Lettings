from django.test import TestCase
from django.contrib.auth.models import User

from profiles.models import Profile


class ProfilesModelsTests(TestCase):
    """
    Tests models of profiles application.
    """

    def setUp(self):
        """
        Set up the test environment by creating user and profile.
        This method is called before every test method to prepare the objects
        required for testing.
        """

        self.user = User.objects.create(username='testuser')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Toulouse')

    def test_profile_user(self):
        """
        Test the profile creation.

        Ensures that profile object is successfully created and
        his username is correct.
        """

        self.assertEqual(self.profile.user.username, 'testuser')

    def test_profile_str(self):
        """
        Test the string representation.

        Ensures that the __str__ method returns the correct username.
        """

        self.assertEqual(str(self.profile), 'testuser')
