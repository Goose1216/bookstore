from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomePageTests(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get(reverse('about'))

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_url_resolves_aboutpageview(self):
        view = resolve(reverse('about'))
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
