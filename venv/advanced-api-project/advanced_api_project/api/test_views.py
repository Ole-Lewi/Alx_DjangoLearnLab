from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Authenticate the user
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create books
        self.book1 = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            publication_year=1998,
            author=self.author
        )
    def test_get_books(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two books exist

    def test_create_book(self):
        data = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "publication_year": 1999,
            "author": self.author.id,
        }
        response = self.client.post("/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # New book added

    def test_update_book(self):
        data = {"title": "Harry Potter and the Philosopher's Stone - Updated"}
        response = self.client.put(f"/books/{self.book1.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Harry Potter and the Philosopher's Stone - Updated")
    
    def test_delete_book(self):
        response = self.client.delete(f"/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # One book removed

    def test_filter_books_by_author(self):
        response = self.client.get(f"/books/?author={self.author.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books belong to the same author

    def test_search_books_by_title(self):
        response = self.client.get("/books/?search=Philosopher")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book matches the title search

