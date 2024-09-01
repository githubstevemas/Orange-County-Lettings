from django.test import TestCase
from django.contrib.auth.models import User

from profiles.models import Profile


class ProfilesModelsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Toulouse')

    def test_profile_user(self):
        self.assertEqual(self.profile.user.username, 'testuser')

    def test_profile_str(self):
        self.assertEqual(str(self.profile), 'testuser')
