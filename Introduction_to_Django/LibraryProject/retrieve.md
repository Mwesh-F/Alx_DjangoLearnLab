from bookshelf.models import Book

# Retrieve the book using .get()
book = Book.objects.get(title="1984")

# Display all attributes
print(book.title)
print(book.author)
print(book.publication_year)

# Output:
# 1984
# George Orwell
# 1949
