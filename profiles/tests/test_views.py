from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from profiles.models import Profile


class ProfilesViewsTests(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='testuser')
        self.profile = Profile.objects.create(user=self.user,
                                              favorite_city='Toulouse')

    def test_profiles_index_view(self):

        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profiles")

    def test_profile_view(self):

        response = self.client.get(reverse('profiles:profile',
                                           args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, "Toulouse")
