from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# RegisterForm class is inherting from class UserCreationForm
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Meta class holds the information regarding RegisterForm class
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
