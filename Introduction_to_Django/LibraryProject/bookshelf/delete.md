# Delete Operation

**Command:**
```python
# Delete the book instance
retrieved_book.delete()

# Confirm the deletion by trying to retrieve all books
remaining_books = Book.objects.all()
print(remaining_books)

#expected output
# Query returns an empty list if the book was successfully deleted.
# Output: []
