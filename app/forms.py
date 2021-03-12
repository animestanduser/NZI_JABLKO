from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions
from .models import Profile
from .models import Post







class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username','first_name', 'email', 'password1', 'password2')
        


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('imie', 'nazwisko','opis', 'image', 'przedmiot', 'miejscowosc')