from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTest(TestCase):

    @classmethod
    def setUp(cls):
        cls.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )

    def test_information(self):
        self.assertEqual(self.book.title, 'Harry Potter')
        self.assertEqual(self.book.author, 'JK Rowling')
        self.assertEqual(self.book.price, '25.00')
        self.assertEqual(Book.objects.all().count(), 1)

    def test_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        fake_response = self.client.get('books/999')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(fake_response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_detail.html')
