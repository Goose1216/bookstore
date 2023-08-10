from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Book, Review

class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='reviewuser',
            password='1234',
            email='review@mail.ru',
        )

        cls.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )

        cls.review = Review.objects.create(
            book=cls.book,
            review='testreview',
            author=cls.user,
        )

    def test_information(self):
        self.assertEqual(self.book.title, 'Harry Potter')
        self.assertEqual(self.book.author, 'JK Rowling')
        self.assertEqual(self.book.price, '25.00')
        self.assertEqual(Book.objects.all().count(), 1)
        self.assertIs(self.book, self.review.book)
        self.assertIs(self.user, self.review.author)
        self.assertEqual(self.review.review, 'testreview')

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

    def test_book_list_view_for_logged_in_user(self):  # new
        self.client.login(email="reviewuser@email.com", password="testpass123")
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")

