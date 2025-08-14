from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, UserUpdateForm

def user_login(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("profile")
		else:
			messages.error(request, "Invalid username or password.")
	return render(request, "blog/login.html")

def user_logout(request):
	logout(request)
	return redirect("login")

def register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Registration successful. Please log in.")
			return redirect("login")
	else:
		form = CustomUserCreationForm()
	return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
	if request.method == "POST":
		form = UserUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, "Profile updated successfully.")
			return redirect("profile")
	else:
		form = UserUpdateForm(instance=request.user)
	return render(request, "blog/profile.html", {"form": form})

# Create your views here.
