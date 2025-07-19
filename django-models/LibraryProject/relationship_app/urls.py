from django.urls import path
from .views import list_books, LibraryDetailView, library_list, author_detail, register_view, login_view, logout_view

app_name = 'relationship_app'

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Function-based view for listing all libraries
    path('libraries/', library_list, name='library_list'),
    
    # Function-based view for author detail
    path('author/<int:author_id>/', author_detail, name='author_detail'),
] 
