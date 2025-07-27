from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating new users in the admin interface.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo')


class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating existing users in the admin interface.
    """
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo', 'bio', 'phone_number')


class UserRegistrationForm(UserCreationForm):
    """
    Form for user registration.
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make email field required
        self.fields['email'].required = True
        # Make username optional
        self.fields['username'].required = False


class UserProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'profile_photo', 'bio', 'phone_number')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        } 


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField() 
