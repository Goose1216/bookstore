from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignUpPageView

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test',
            email='test@mail.ru',
            password='test'
        )
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@mail.ru')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='test',
            email='test@mail.ru',
            password='test'
        )
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@mail.ru')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignUpPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@mail.ru'

    def setUp(self):
        self.response = self.client.get(reverse('account_signup'))

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')

    def test_signup_form(self):
        user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
