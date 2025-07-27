from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm, UserProfileUpdateForm

User = get_user_model()


def register(request):
    """
    View for user registration.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Redirect to home page or dashboard
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    """
    View for displaying and updating user profile.
    """
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileUpdateForm(instance=request.user)
    
    return render(request, 'accounts/profile.html', {'form': form}) 