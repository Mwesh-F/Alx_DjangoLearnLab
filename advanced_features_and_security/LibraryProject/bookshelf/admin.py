from django.contrib import admin
from .models import Book

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in list view
    search_fields = ('title', 'author')                     # Enable search
    list_filter = ('publication_year',)                     # Enable filter by year
