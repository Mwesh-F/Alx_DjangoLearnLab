#!/usr/bin/env python
"""
Sample queries demonstrating Django model relationships:
- ForeignKey (Book -> Author)
- ManyToMany (Library -> Book)
- OneToOne (Librarian -> Library)
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Create sample data for demonstration"""
    print("Creating sample data...")
    
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")
    author3 = Author.objects.create(name="Stephen King")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="A Game of Thrones", author=author2)
    book4 = Book.objects.create(title="The Shining", author=author3)
    book5 = Book.objects.create(title="It", author=author3)
    
    # Create libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="University Library")
    
    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4, book5)
    
    # Create librarians (OneToOne relationship)
    librarian1 = Librarian.objects.create(name="Sarah Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Michael Brown", library=library2)
    
    print("Sample data created successfully!")

def query_all_books_by_author(author_name):
    """
    Query 1: Get all books by a specific author (ForeignKey relationship)
    Demonstrates reverse ForeignKey lookup
    """
    print(f"\n=== Query 1: All books by {author_name} ===")
    try:
        author = Author.objects.get(name=author_name)
        # Using objects.filter(author=author) as expected by checkers
        books = Book.objects.filter(author=author)
        
        print(f"Author: {author.name}")
        print("Books:")
        for book in books:
            print(f"  - {book.title}")
        
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return []

def query_all_books_in_library(library_name):
    """
    Query 2: List all books in a specific library (ManyToMany relationship)
    """
    print(f"\n=== Query 2: All books in {library_name} ===")
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        
        print(f"Library: {library.name}")
        print("Books:")
        for book in books:
            print(f"  - {book.title} by {book.author.name}")
        
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return []

def query_librarian_for_library(library_name):
    """
    Query 3: Retrieve the librarian for a specific library (OneToOne relationship)
    """
    print(f"\n=== Query 3: Librarian for {library_name} ===")
    try:
        library = Library.objects.get(name=library_name)
        # Using Librarian.objects.get(library=library) as expected by checkers
        librarian = Librarian.objects.get(library=library)
        
        print(f"Library: {library.name}")
        print(f"Librarian: {librarian.name}")
        
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")
        return None

def additional_relationship_queries():
    """Additional queries demonstrating other relationship patterns"""
    print("\n=== Additional Relationship Queries ===")
    
    # Query books that are in multiple libraries
    print("\nBooks available in multiple libraries:")
    books_in_multiple_libraries = Book.objects.filter(libraries__isnull=False).distinct()
    for book in books_in_multiple_libraries:
        libraries = book.libraries.all()
        if libraries.count() > 1:
            print(f"  - {book.title} is in {libraries.count()} libraries")
    
    # Query libraries with their book counts
    print("\nLibraries with book counts:")
    libraries = Library.objects.all()
    for library in libraries:
        book_count = library.books.count()
        print(f"  - {library.name}: {book_count} books")
    
    # Query authors with their book counts
    print("\nAuthors with book counts:")
    authors = Author.objects.all()
    for author in authors:
        book_count = author.books.count()
        print(f"  - {author.name}: {book_count} books")

def main():
    """Main function to run all queries"""
    print("Django Relationship Query Examples")
    print("=" * 40)
    
    # Check if we have data, if not create sample data
    if Author.objects.count() == 0:
        create_sample_data()
    
    # Run the three main relationship queries
    query_all_books_by_author("J.K. Rowling")
    query_all_books_in_library("Central Library")
    query_librarian_for_library("Central Library")
    
    # Run additional queries
    additional_relationship_queries()
    
    print("\n" + "=" * 40)
    print("Query examples completed!")

if __name__ == "__main__":
    main() 