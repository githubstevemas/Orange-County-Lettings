from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from profiles.models import Profile


class ProfilesViewsTests(TestCase):
    """
    Tests for the views of profiles application.
    """

    def setUp(self):
        """
        Set up the test environment by creating a user and profile.
        This method is called before every test method to prepare the objects
        required for testing.
        """

        self.user = User.objects.create(username='testuser')
        self.profile = Profile.objects.create(user=self.user,
                                              favorite_city='Toulouse')

    def test_profiles_index_view(self):
        """
        Test the profiles index view.

        Ensures that the profiles index page loads successfully and
        returns 200 status code.
        Ensures that contains Profiles.
        """

        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profiles")

    def test_profile_view(self):
        """
        Test the individual profile view.

        Ensures that a specific profile page loads successfully and
        returns 200 status code.
        Ensures that contains username and favorite city.
        """

        response = self.client.get(reverse('profiles:profile',
                                           args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, "Toulouse")
