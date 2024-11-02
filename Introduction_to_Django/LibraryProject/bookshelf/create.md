# Create Operation

**Command:**
```python
# Open the Django shell
python manage.py shell

# Create a Book instance
book_1984 = Book(title="1984", author="George Orwell", published_year=1949)
book_1984.save()

# The instance is created and saved successfully without any output in the shell.
