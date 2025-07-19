from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Function-based view for listing all libraries
    path('libraries/', views.library_list, name='library_list'),
    
    # Function-based view for author detail
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
] 