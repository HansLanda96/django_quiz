from accounts.models import User

from django.test import TestCase


class TestModels(TestCase):
    username = None

    @classmethod
    def setUpTestData(cls):
        cls.username = 'user_1'
        User.objects.create_user(
            username=cls.username,
            password='1123@fsdmfs',
            email='user_1@test.com'
        )

    def setUp(self):
        self.user = User.objects.get(username=self.username)

    def test_avatar_lable_is_correct(self):
        field_label = self.user._meta.get_field('avatar').verbose_name
        self.assertEqual(field_label, 'avatar')

    def test_city_max_length(self):
        meta_info = self.user._meta.get_field('city')
        self.assertEqual(meta_info.max_length, 50)
        self.assertTrue(meta_info.null)
        self.assertTrue(meta_info.blank)

    def test_convert_user_to_string(self):
        self.assertEqual(str(self.user), self.username)
