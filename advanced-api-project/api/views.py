

"""
Views for the API app.

Implements CRUD operations for Book using DRF generic views and permissions.
"""
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as django_filters_rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer



# List all books with filtering, searching, and ordering capabilities
# Filtering: by title, author, publication_year
# Searching: by title, author__name
# Ordering: by title, publication_year
class BookListView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]
	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filterset_fields = ['title', 'author', 'publication_year']
	search_fields = ['title', 'author__name']
	ordering_fields = ['title', 'publication_year']
	ordering = ['title']  # Default ordering


# Retrieve a single book by ID (read-only for unauthenticated users)
class BookDetailView(generics.RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


# Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]


# Update an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]


# Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]
