# Retrieve Operation

**Command:**
```python
# Retrieve and display all attributes of the book created
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)

#Expected output