from .models import Post, Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment here...'})
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


from .models import Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter comma-separated tags (existing or new)",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Django, Python, Tutorial'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags_str = self.cleaned_data.get('tags', '')
        tag_names = [name.strip() for name in tags_str.split(',') if name.strip()]
        if commit:
            instance.save()
            instance.tags.clear()
            for name in tag_names:
                tag_obj, created = Tag.objects.get_or_create(name=name)
                instance.tags.add(tag_obj)
        return instance

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")
