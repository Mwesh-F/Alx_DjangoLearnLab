"""
Unit tests for Book API endpoints in advanced_api_project.

Covers CRUD operations, filtering, searching, ordering, and permissions.
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Author1')
        self.book1 = Book.objects.create(title='Book A', publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title='Book B', publication_year=2021, author=self.author)
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_requires_auth(self):
        data = {'title': 'Book C', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.login(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_requires_auth(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'Book A Updated', 'publication_year': 2020, 'author': self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Book A Updated')

    def test_delete_book_requires_auth(self):
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + '?title=Book A')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book A')

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url + '?search=Book B')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book B')

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url + '?ordering=-publication_year')
        self.assertEqual(response.data[0]['publication_year'], 2021)

"""
How to run tests:
- Run: python manage.py test api
- Tests cover CRUD, filtering, searching, ordering, and permissions for Book endpoints.
"""
