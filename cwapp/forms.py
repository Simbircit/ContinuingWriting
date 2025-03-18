from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginUser(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


class ContinueCreationForm(forms.ModelForm):
    class Meta:
        model = PostContinue
        fields = []


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
