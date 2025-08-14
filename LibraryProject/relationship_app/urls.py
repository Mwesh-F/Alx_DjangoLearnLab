from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, library_list, author_detail, register, CustomLoginView, CustomLogoutView, admin_view, librarian_view, member_view, add_book, edit_book, delete_book

app_name = 'relationship_app'

urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Role-based access control URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Book management URLs with custom permissions
    path('add_book/', add_book, name='add_book'),
    path('edit_book/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Function-based view for listing all libraries
    path('libraries/', library_list, name='library_list'),
    
    # Function-based view for author detail
    path('author/<int:author_id>/', author_detail, name='author_detail'),
] 