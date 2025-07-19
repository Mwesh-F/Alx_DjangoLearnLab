from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Book, Library, Author, Librarian
from .models import Library

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

def register(request):
    """
    User registration view using Django's built-in UserCreationForm
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('relationship_app:list_books')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    """
    Custom login view using Django's built-in LoginView
    """
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    """
    Custom logout view using Django's built-in LogoutView
    """
    template_name = 'relationship_app/logout.html'
