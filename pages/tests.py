from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

class HomePageTests(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )