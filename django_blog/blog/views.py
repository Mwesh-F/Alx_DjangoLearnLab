from django.views.generic import ListView
# View to filter posts by tag using django-taggit
class PostByTagListView(ListView):
	model = Post
	template_name = 'blog/post_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		tag_slug = self.kwargs.get('tag_slug')
		return Post.objects.filter(tags__slug=tag_slug)
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


from django.db.models import Q
from .models import Tag

def post_search(request):
	query = request.GET.get('q', '')
	posts = Post.objects.all()
	if query:
		posts = Post.objects.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(tags__name__icontains=query)
		).distinct()
	return render(request, 'blog/post_search.html', {'posts': posts, 'query': query})

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

class PostListView(ListView):
	model = Post
	template_name = 'blog/post_list.html'
	context_object_name = 'posts'
	ordering = ['-published_date']


from .models import Comment
from .forms import CommentForm

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['comments'] = self.object.comments.order_by('-created_at')
		context['comment_form'] = CommentForm()
		return context

from django.shortcuts import get_object_or_404, redirect

class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'blog/comment_form.html'

	def form_valid(self, form):
		post = get_object_or_404(Post, pk=self.kwargs['post_id'])
		form.instance.post = post
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.post.get_absolute_url() if hasattr(self.object.post, 'get_absolute_url') else f"/posts/{self.object.post.pk}/"

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Comment
	form_class = CommentForm
	template_name = 'blog/comment_form.html'

	def test_func(self):
		comment = self.get_object()
		return self.request.user == comment.author

	def get_success_url(self):
		return self.object.post.get_absolute_url() if hasattr(self.object.post, 'get_absolute_url') else f"/posts/{self.object.post.pk}/"

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	template_name = 'blog/comment_confirm_delete.html'

	def test_func(self):
		comment = self.get_object()
		return self.request.user == comment.author

	def get_success_url(self):
		return self.object.post.get_absolute_url() if hasattr(self.object.post, 'get_absolute_url') else f"/posts/{self.object.post.pk}/"

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/post_form.html'
	success_url = reverse_lazy('post-list')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/post_form.html'
	success_url = reverse_lazy('post-list')

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'blog/post_confirm_delete.html'
	success_url = reverse_lazy('post-list')

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author
