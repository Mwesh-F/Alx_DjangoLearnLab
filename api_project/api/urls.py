from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
