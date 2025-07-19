from bookshelf.models import Book

# Update title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify
print(book.title)

# Output:
# Nineteen Eighty-Four
