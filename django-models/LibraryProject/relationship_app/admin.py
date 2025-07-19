from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count']
    search_fields = ['name']
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'library_count']
    list_filter = ['author']
    search_fields = ['title', 'author__name']
    
    def library_count(self, obj):
        return obj.libraries.count()
    library_count.short_description = 'Available in Libraries'

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count', 'librarian_name']
    search_fields = ['name']
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'
    
    def librarian_name(self, obj):
        try:
            return obj.librarian.name
        except Librarian.DoesNotExist:
            return "No librarian assigned"
    librarian_name.short_description = 'Librarian'

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ['name', 'library']
    search_fields = ['name', 'library__name']
    list_filter = ['library']
