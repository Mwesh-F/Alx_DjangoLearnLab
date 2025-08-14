from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book

# Create your views here.

def home(request):
    """Home view for the application."""
    books = Book.objects.all()[:5]  # Get first 5 books
    context = {
        'books': books,
        'user': request.user,
    }
    return render(request, 'home.html', context)

@login_required
def user_dashboard(request):
    """Dashboard view for authenticated users."""
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard.html', context)
