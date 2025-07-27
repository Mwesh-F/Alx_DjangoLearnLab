from django.urls import path
from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
] 