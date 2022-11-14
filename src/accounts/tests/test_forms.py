from accounts.forms import UserRegisterForm

from django.test import TestCase


class TestForms(TestCase):
    def setUp(self):
        self.username = 'user_1'
        self.password = '1123@fsdmfs'
        self.email = 'user_1@gmail.com'

    def test_register_form_validate_data(self):
        form = UserRegisterForm(
            data={
                'username': self.username,
                'email': self.email,
                'password1': self.password,
                'password2': self.password,
            }
        )
        self.assertTrue(form.is_valid())

    def test_register_form_no_data(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
