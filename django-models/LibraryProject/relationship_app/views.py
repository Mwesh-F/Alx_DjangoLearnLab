from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Book, Library, Author, Librarian

# Create your views here.

def list_books(request):
    """
    Function-based view that lists all books stored in the database.
    Renders a simple text list of book titles and their authors.
    """
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library,
    listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context if needed
        return context

def library_list(request):
    """
    Function-based view that lists all libraries.
    """
    libraries = Library.objects.all().prefetch_related('books')
    return render(request, 'relationship_app/library_list.html', {'libraries': libraries})

def author_detail(request, author_id):
    """
    Function-based view that shows details for a specific author.
    """
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all()
    return render(request, 'relationship_app/author_detail.html', {
        'author': author,
        'books': books
    })
