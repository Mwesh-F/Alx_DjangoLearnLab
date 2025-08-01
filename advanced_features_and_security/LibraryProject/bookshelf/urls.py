from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='bookshelf:home'), name='logout'),
    path('book_list/', views.book_list, name='book_list'),
] 
