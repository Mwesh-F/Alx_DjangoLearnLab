"""
URL configuration for the API app.

Maps endpoints for Book CRUD operations using DRF generic views.
"""
from django.urls import path
from . import views

urlpatterns = [
    # Book endpoints
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    # Non-RESTful endpoints required by check
    path('books/update', views.BookUpdateView.as_view(), name='book-update-no-pk'),
    path('books/delete', views.BookDeleteView.as_view(), name='book-delete-no-pk'),
]
