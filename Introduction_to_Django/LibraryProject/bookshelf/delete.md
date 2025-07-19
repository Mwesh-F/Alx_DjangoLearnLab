from bookshelf.models import Book

# Delete book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()

# Output:
# <QuerySet []>
