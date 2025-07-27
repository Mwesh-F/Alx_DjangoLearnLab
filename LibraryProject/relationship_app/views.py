from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseForbidden
from .models import Book, Library, Author, Librarian, UserProfile
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

# Role-based access control functions
def is_admin(user):
    """Check if user has Admin role"""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Check if user has Librarian role"""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Check if user has Member role"""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    """
    Admin view that only users with 'Admin' role can access
    """
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    """
    Librarian view accessible only to users with 'Librarian' role
    """
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    """
    Member view for users with 'Member' role
    """
    return render(request, 'relationship_app/member_view.html')

# Book management views with custom permissions
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """
    View to add a new book - requires can_add_book permission
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        
        if title and author_id:
            try:
                author = Author.objects.get(id=author_id)
                book = Book.objects.create(title=title, author=author)
                messages.success(request, f'Book "{book.title}" added successfully!')
                return redirect('relationship_app:list_books')
            except Author.DoesNotExist:
                messages.error(request, 'Author not found.')
        else:
            messages.error(request, 'Please provide both title and author.')
    
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    """
    View to edit an existing book - requires can_change_book permission
    """
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        
        if title and author_id:
            try:
                author = Author.objects.get(id=author_id)
                book.title = title
                book.author = author
                book.save()
                messages.success(request, f'Book "{book.title}" updated successfully!')
                return redirect('relationship_app:list_books')
            except Author.DoesNotExist:
                messages.error(request, 'Author not found.')
        else:
            messages.error(request, 'Please provide both title and author.')
    
    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {
        'book': book,
        'authors': authors
    })

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """
    View to delete a book - requires can_delete_book permission
    """
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book_title = book.title
        book.delete()
        messages.success(request, f'Book "{book_title}" deleted successfully!')
        return redirect('relationship_app:list_books')
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})
