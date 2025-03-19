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
        fields = ['author', 'title', 'description', 'start_title', 'post_start', 'end_title', 'post_end', 'status',
                  'image', 'continues_max']


class ContinueCreationForm(forms.ModelForm):
    class Meta:
        model = PostContinue
        fields = []


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class ProfileAvatarUpdate(forms.ModelForm):

    class Meta:

        model = Profile
        fields = ['avatar']


class ProfileEdit(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'first_name', 'email']