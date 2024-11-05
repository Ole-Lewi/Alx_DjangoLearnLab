import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  # Replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author.name}: {[book.title for book in books]}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library.name}: {[book.title for book in books]}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")

if __name__ == "__main__":
    # Example queries
    books_by_author("Author Name")  # Replace with an actual author's name
    books_in_library("Library Name")  # Replace with an actual library's name
    librarian_for_library("Library Name")  # Replace with an actual library's name
