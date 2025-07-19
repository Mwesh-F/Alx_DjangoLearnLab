from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, library_list, author_detail, register, CustomLoginView, CustomLogoutView

app_name = 'relationship_app'

urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Function-based view for listing all libraries
    path('libraries/', library_list, name='library_list'),
    
    # Function-based view for author detail
    path('author/<int:author_id>/', author_detail, name='author_detail'),
] 
