# Relationship App

This Django app demonstrates complex relationships between entities using ForeignKey, ManyToMany, and OneToOne fields.

## Models

### Author
- **name**: CharField (max_length=100)
- **Purpose**: Represents book authors

### Book
- **title**: CharField (max_length=200)
- **author**: ForeignKey to Author (CASCADE delete, related_name='books')
- **Purpose**: Represents books with a foreign key relationship to authors

### Library
- **name**: CharField (max_length=100)
- **books**: ManyToManyField to Book (related_name='libraries')
- **Purpose**: Represents libraries that can have multiple books

### Librarian
- **name**: CharField (max_length=100)
- **library**: OneToOneField to Library (CASCADE delete, related_name='librarian')
- **Purpose**: Represents librarians with a one-to-one relationship to libraries

## Relationship Types Demonstrated

1. **ForeignKey (Book → Author)**
   - Each book belongs to one author
   - An author can have multiple books
   - Reverse lookup: `author.books.all()`

2. **ManyToMany (Library ↔ Book)**
   - A library can have multiple books
   - A book can be in multiple libraries
   - Access: `library.books.all()` or `book.libraries.all()`

3. **OneToOne (Librarian → Library)**
   - Each library has exactly one librarian
   - Each librarian works at exactly one library
   - Access: `library.librarian` or `librarian.library`

## Sample Queries

The `query_samples.py` script demonstrates:

1. **Query all books by a specific author** (ForeignKey relationship)
2. **List all books in a library** (ManyToMany relationship)
3. **Retrieve the librarian for a library** (OneToOne relationship)

## Running the Sample Queries

```bash
cd LibraryProject
python relationship_app/query_samples.py
```

## Admin Interface

All models are registered in the Django admin interface with custom list displays and search functionality:

- **Author**: Shows name and book count
- **Book**: Shows title, author, and library count
- **Library**: Shows name, book count, and librarian
- **Librarian**: Shows name and assigned library

## Database Migrations

The app includes initial migrations that create all necessary database tables and relationships.

## Usage Examples

```python
# ForeignKey relationship
author = Author.objects.get(name="J.K. Rowling")
books = author.books.all()  # Get all books by this author

# ManyToMany relationship
library = Library.objects.get(name="Central Library")
books = library.books.all()  # Get all books in this library

# OneToOne relationship
library = Library.objects.get(name="Central Library")
librarian = library.librarian  # Get the librarian for this library
``` 